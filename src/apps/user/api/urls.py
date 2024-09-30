from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter

# Views

from src.apps.user.api.views import (
    RegisterUser,
    LoginUser
)

router = DefaultRouter()

urlpatterns = [
    path("register/", RegisterUser.as_view()),
    path("login/", LoginUser.as_view()),
]
