from django.urls import path
from django.urls import include

# views
from src.apps.home.dash.views import (catalog, homepage)

urlpatterns = [
    path("catalog/", catalog, name="catalog-dash"),
    path("", homepage, name="homepage-dash"),
]