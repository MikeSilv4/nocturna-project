from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter

# Views

from src.apps.user.api.views import (
    RegisterUser,
    LoginUser,
    ForgotPassword
)

router = DefaultRouter()
router.register(r'create', RegisterUser, basename='register')
router.register(r'login', LoginUser, basename='login')
router.register(r'forgot-password', ForgotPassword, basename='forgot_password')

urlpatterns = [
    
] + router.urls
