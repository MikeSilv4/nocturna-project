from django.urls import path
from django.urls import include

# views
from src.apps.home.dash.views import (
    catalog
)

urlpatterns = [
    path("catalog/", catalog, name="catalog-dash"),
]