from rest_framework import serializers
from src.apps.items.models import Items


class ItemsAllFieldsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Items
        fields = "__all__"
