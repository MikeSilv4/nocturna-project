from rest_framework import serializers

# models
from src.apps.user.models import CustomUser

class CreateUserSerializerClass(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = '__all__'

class LoginUserSerializerClass(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ["username", "password"]
