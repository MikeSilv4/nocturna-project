from django.urls import path
from django.urls import include

app_name = 'src.apps.user.dash'

# views
from src.apps.user.dash.views import (
    Login,
    ForgotPassword,
    CreateAccount
)

urlpatterns = [
    path("login/", Login, name="login-dash"),
    path("forgot-password/", ForgotPassword, name="forgot-password-dash"),
    path("create-account/", CreateAccount, name="create-dash"),
]