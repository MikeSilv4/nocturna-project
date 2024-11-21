from rest_framework import serializers
from src.apps.sales.models import Sales 

class SalesAllFieldsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sales
        fields = "__all__"

class SaleSerializerrClass(serializers.Serializer):

    user_id = serializers.CharField(required=True)
    item_id = serializers.CharField(required=True)
    quantity = serializers.DecimalField(required=True, max_digits=20, decimal_places=4)

class SaleBuySerializerrClass(serializers.Serializer):

    value = serializers.FloatField(required=True)