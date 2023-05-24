from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.user_authentication.serializers import *
from django.contrib.auth import authenticate
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from rest_framework import generics, permissions
from app.user_authentication import services



# Create your views here.

class UserRegistrationView(APIView):
    def get(self, request):
        res = services.view_users(request=request)
        return Response(res)    
    def post(self,request,format=None):
        res = services.user_registration(request=request)
        return Response(res)
