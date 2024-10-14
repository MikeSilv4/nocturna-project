from rest_framework import serializers
from src.apps.sales.models import Sales 

class SalesAllFieldsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sales
        fields = "__all__"
