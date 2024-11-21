from django.urls import path
from django.urls import include

# views
from src.apps.sales.dash.views import (
    sale_item,
    bag
)

urlpatterns = [
    path("item/", sale_item, name="sale-dash"),
    path("bag/", bag, name="bag-dash"),
]