from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin

from src.apps.sales.models import (
    Sales
)

from src.apps.items.models import (
    Items
)

from src.apps.sales.api.serializers import (
    SalesAllFieldsSerializer,
    SaleSerializerrClass
)

class SalesViewSet(viewsets.GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin):

    serializer_class = SalesAllFieldsSerializer
    queryset = Sales.objects.all()
    autentication_class = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'create':
            return SaleSerializerrClass  
        else:
            return self.serializer_class
        return super().get_serializer_class()

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer_class()(data=request.data)
        serializer.is_valid()
        data = serializer.data

        item = Items.objects.filter(id=data.get("item_id", None)).first()
        print(type(data.get("quantity", None)))
        if not item:
            return Response("item nao existente", status=status.HTTP_400_BAD_REQUEST)

        if item.stock_quantity - float(data.get("quantity", None)) < 0:
            return Response("quantidade maior do que a em estoque", status=status.HTTP_400_BAD_REQUEST)
        else:
            item.stock_quantity = item.stock_quantity - float(data.get("quantity", None))

            sale_data = {
                "name" : item.name,
                "brand" : item.brand,
                "model" : item.model,
                "description" : item.description,
                "value" : item.value,
                "quantity" : data.get("quantity", None),
                "user" : data.get("user_id", None)
            }

            serializer = SalesAllFieldsSerializer(data=sale_data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            item.save()

            return Response("ok", status=status.HTTP_202_ACCEPTED)
