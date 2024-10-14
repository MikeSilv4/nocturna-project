from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated

from src.apps.sales.models import (
    Sales
)

from src.apps.items.models import (
    Items
)

from src.apps.sales.api.serializers import (
    SalesAllFieldsSerializer
)

class SalesViewSet(viewsets.ModelViewSet):

    serializer_class = SalesAllFieldsSerializer
    queryset = Sales.objects.all()
    autentication_class = (IsAuthenticated,)

    def perform_create(self, serializer):

        item = self.request.data["id"]
        item = Items.objects.get(id=item)

        if item.stock_quantity - self.request.data["quantity"] > 0:
            raise ValueError("Quantidade nao pode ser menor que 0")

        item.stock_quantity = item.stock_quantity - self.request.data["quantity"]
        item.save()
        serializer.save()