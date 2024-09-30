from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponseRedirect

# models

from src.apps.user.models import CustomUser

class RegisterUser(APIView):
        
        def post(self, request):

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
        
class LoginUser(APIView):

     def post(self, request):

        data = request.data
        username = data['email']
        password = data['password']
        user = authenticate(username=username, password=password)

        if user:

            user_data = CustomUser.objects.get(username=username)
            login(request, user)

            return HttpResponseRedirect("/dash/organizer/home/event-create/")

        else:
            return Response('Incorrect data...', status=status.HTTP_400_BAD_REQUEST)