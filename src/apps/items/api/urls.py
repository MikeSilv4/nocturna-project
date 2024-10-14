from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter

# Views
from src.apps.items.api.views import (
    ItemsViewSet
)

router = DefaultRouter()
router.register(r'items', ItemsViewSet, basename='items_view_set')

urlpatterns = [
    
] + router.urls
