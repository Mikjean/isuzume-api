from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('user/register/', RegisterView.as_view(), name="register"),
    path('user/email-verify/', verifyEmail.as_view(), name="verify-email"),
    path('user/login/', LoginAPIView.as_view(), name="login"),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
    path('user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/request-reset-email/', RequestPasswordResetEmail.as_view(), name="request-reset-email"),
    path('user/password-reset/<uidb64>/<token>/', PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('password-reset-complete', SetNewPasswordAPIView.as_view(), name='password-reset-complete')
    
]