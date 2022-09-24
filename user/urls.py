from django.urls import path, include
from .views import RegistrationView, LoginView, ChangePasswordView, ProfileViewSet
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'profile', ProfileViewSet, basename='user-profiles')

app_name = 'user'

urlpatterns = [
    path('user/register/', RegistrationView.as_view(), name='register'),
    path('user/login/', LoginView.as_view(), name='login'),
    # path('user/logout/', LogoutView.as_view(), name='logout'),
    path('user/change-password/', ChangePasswordView.as_view(), name='password-change'),
    path('user/token-refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path("", include(router.urls)),
]
