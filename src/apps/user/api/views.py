from rest_framework.views import APIView
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin
)
from rest_framework.viewsets import (
    GenericViewSet
)
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import HttpResponseRedirect
from rest_framework.decorators import action
from django.contrib.auth import logout
import random
from django.core.mail import EmailMessage
from django.conf import settings
# models

from src.apps.user.models import CustomUser
from src.apps.user.api.serializers import (
   CreateUserSerializerClass,
   LoginUserSerializerClass,
   UserDeleteSerializerClass
)

class RegisterUser(GenericViewSet, CreateModelMixin):
        
    serializer_class = CreateUserSerializerClass           
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny]

    def create(self, request):

        data = request.data
        cpf = data['cpf']
        born_date = data['born_date']
        email = data['email']
        first_name = data['first_name']
        last_name = data['last_name']
        password = data['password']

        user = CustomUser.objects.filter(username=email).first()

        if user:
            return Response('This user arredy exist!', status=status.HTTP_400_BAD_REQUEST)
        
        user = get_user_model()
        user = user.objects.create_user(email=email, password=password, born_date=born_date, cpf=cpf, first_name=first_name, last_name=last_name)

        return Response({"status" : "ok", "details" : "User created"}, status=status.HTTP_200_OK)
    
class LoginUser(GenericViewSet, CreateModelMixin, DestroyModelMixin):

    serializer_class = LoginUserSerializerClass
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny]
    
    def get_serializer_class(self):
        if self.action == 'create':
            return LoginUserSerializerClass  
        elif self.action == 'destroy':
            return LoginUserSerializerClass  
        else:
            return None
        return super().get_serializer_class()

    def create(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(request, username=serializer.data.get("username", None), password=serializer.data.get("password", None))

        if user:
            login(request, user)
            return Response("logado", status=status.HTTP_200_OK)
        else:
            return Response('Incorrect data...', status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(request, username=serializer.data.get("username", None), password=serializer.data.get("password", None))

        if user:
            CustomUser.objects.filter(username=email).first().delete()
            return Response("Deleted", status=status.HTTP_200_OK)
        else:
            return Response("Unautorizated", status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['GET'])
    def logout_user(self, request):
        logout(request)

        return Response("logout", status=status.HTTP_200_OK)

class ForgotPassword(GenericViewSet, CreateModelMixin):
        
    serializer_class = CreateUserSerializerClass           
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny]

    def create(self, request):
        try:
            email = request.data.get("email", None)
            user = CustomUser.objects.get(username=email)
            new_password = "".join([str(random.randint(1, 100)) for i in range(20)])
            user.set_password(new_password)
            user.save()

            email = EmailMessage(subject='Nova senha', body=f"Ola, sua senha provisoria e '{new_password}'",
                            from_email=settings.EMAIL_HOST_USER,
                            to=[email])
            email.send()
            return Response('Enviado', status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response('Usuario nao existe', status=status.HTTP_400_BAD_REQUEST)