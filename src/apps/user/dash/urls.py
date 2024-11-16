from django.urls import path
from django.urls import include

# views
from src.apps.user.dash.views import (login, create, view,)

urlpatterns = [
    path("login/", login, name="login-dash"),
    path("create/", create, name="create-dash"),
    path("view/", view, name="view-dash"),
]