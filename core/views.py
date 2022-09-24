from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response


class BaseModelViewSet(viewsets.ModelViewSet):
    update_status_serializer_class = None
    service_class = None

    @action(methods=['patch'], detail=True, url_path='update-status')
    def update_status(self, request, pk):
        instance = self.get_object()
        if self.request.user.user_type == "Vendor" or self.request.user.user_type == "Admin":
            serializer = self.update_status_serializer_class(instance, data=request.data)
            serializer.is_valid(raise_exception=True)        
            self.service_class.update_status(request, instance, serializer.validated_data)
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response({'details': 'You do not have permission!'}, status=status.HTTP_401_UNAUTHORIZED)