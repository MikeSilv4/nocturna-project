from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from src.apps.items.models import (
    Items
)

from src.apps.items.api.serializers import (
    ItemsAllFieldsSerializer
)

class ItemsViewSet(viewsets.ModelViewSet):

    serializer_class = ItemsAllFieldsSerializer
    queryset = Items.objects.all()
    autentication_class = (IsAuthenticated,)

