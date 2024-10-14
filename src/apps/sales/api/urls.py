from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter

# views
from src.apps.sales.api.views import (
    SalesViewSet
)

router = DefaultRouter()
router.register(r"sales", SalesViewSet, basename="sales_view")

urlpatterns = [
] + router.urls