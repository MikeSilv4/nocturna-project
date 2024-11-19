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

class UserDeleteSerializerClass(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ["password"]

class CreateUserSerializerClass(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password', 'born_date', 'cpf']

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password) 
            user.save()
        return user