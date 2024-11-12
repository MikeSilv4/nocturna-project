from django.urls import path
from django.urls import include

# views
from src.apps.user.dash.views import (
    login
)

urlpatterns = [
    path("login/", login, name="login-dash"),
]