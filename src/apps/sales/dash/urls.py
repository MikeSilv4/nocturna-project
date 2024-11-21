from django.urls import path
from django.urls import include

app_name = 'src.apps.sales.dash'

# views
from src.apps.sales.dash.views import (
    sale_item,
    bag,
    favorite_item,
    view_item,
    promotions
)

urlpatterns = [
    path("item/", sale_item, name="sale-dash"),
    path("bag/", bag, name="bag-dash"),
    path("favorite_item/", favorite_item, name="favorite_item-dash"),
    path("view_item/", view_item, name="view_item-dash"),
    path("promotions/", promotions, name="promotions-dash"),
]