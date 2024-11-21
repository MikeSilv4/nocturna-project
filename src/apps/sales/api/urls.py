from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter

# views
from src.apps.sales.api.views import (
    SalesViewSet,
    GeneratePay
)

router = DefaultRouter()
router.register(r"sales", SalesViewSet, basename="sales_view")
router.register(r"pay", GeneratePay, basename="GeneratePay")

urlpatterns = [
] + router.urls