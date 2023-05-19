from django.shortcuts import render
from django.contrib.auth.models import User
import jwt
from rest_framework.authentication import get_authorization_header
from rest_framework.response import Response

from django.http import JsonResponse
from rest_framework import status
# Create your views here.
from rest_framework.decorators import api_view
from .seializer import UserSerializer

@api_view(["GET"])
def authentication_view(request):
    authHeader=get_authorization_header(request=request)
    auth=str(authHeader).split(' ')
    if auth[-1] is not None:
        payload=jwt.decode(auth[-1][:-1],algorithms=['HS256'],key="hello ji kaise ho ?")
        user_object=User.objects.get(username=payload['name'])
        serialized_user_data=UserSerializer(user_object)
        return Response(data=serialized_user_data.data,status=status.HTTP_200_OK)
        
    else:
        return Response(data={"data":"Error"},status=status.HTTP_400_BAD_REQUEST)
    

@api_view(["GET"])
def say_hello(request):
    return Response(data={"result":"hey hello,{}".format(request.user.username)},status=status.HTTP_200_OK)