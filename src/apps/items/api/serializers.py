from rest_framework import serializers
from src.apps.items.model import Items


class ItemsAllFieldsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Items
        fields = "__all__"