from django.contrib.auth import authenticate, login
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView

from .utils import get_tokens_for_user
from .serializers import (
    RegistrationSerializer,
    PasswordChangeSerializer,
    ProfileSerializer,
    UserSerializer,
    LogoutSerializer,
    LoginSerializer
)
from .models import Profile, User


class RegistrationView(APIView):
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        if 'email' not in request.data or 'password' not in request.data:
            return Response({'details': 'Credentials missing'}, status=status.HTTP_400_BAD_REQUEST)
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            auth_data = get_tokens_for_user(request.user)
            return Response({'details': 'Login Success', **auth_data}, status=status.HTTP_200_OK)
        return Response({'details': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutAPIView(GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'details': 'Logout successful.'}, status=status.HTTP_204_NO_CONTENT)


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = PasswordChangeSerializer

    def post(self, request):
        serializer = self.serializer_class(context={'request': request}, data=request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.validated_data['new_password'] == serializer.validated_data['new_password2']:
            request.user.set_password(serializer.validated_data['new_password'])
            request.user.save()
            return Response({'details': 'Password changed successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'details': 'New passwords does not match'}, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get']


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.validated_data['user'] == self.request.user:
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'details': 'You do not have permission to perform this!'},
                            status=status.HTTP_401_UNAUTHORIZED)
