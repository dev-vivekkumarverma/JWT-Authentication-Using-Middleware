
from typing import Any
import json
from django.contrib.auth.models import User
from rest_framework.response import Response
import requests
from rest_framework.authentication import get_authorization_header
class CustomMiddleware:
    def __init__(self,get_response) -> None:
        self.get_response=get_response
        self.ignore_list=['/auth/','/admin/']
    def __call__(self,request):
        if request.path not in self.ignore_list:
            url='http://localhost:8000/auth/'
            auth_header=get_authorization_header(request=request)
            header={"Authorization":auth_header}
            resp=requests.get(url,headers=header)
            if resp.status_code!=200:
                return Response(data={"data":"User not found"})
            json_content=resp.json()
            new_user=User()
            new_user.pk=json_content.get("id","")
            new_user.username=json_content.get("username","")
            new_user.is_active=json_content.get("is_active","")
            new_user.password=json_content.get("password","")
            new_user.email=json_content.get("email","")
            request.user=new_user
        response=self.get_response(request)
        return response
