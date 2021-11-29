from django.urls import path
from .views import *

urlpatterns = [
    path('user/register/', RegisterView.as_view(), name="register"),
    path('email-verify/', verifyEmail.as_view(), name="verify-email"),
    path('user/login/', LoginAPIView.as_view(), name="login"),
    
]