from os import access
from django.db.models.query import QuerySet
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import authentication
from rest_framework.authtoken.models import Token
from django.http.response import JsonResponse
from django.core.serializers import serialize
from django.core.mail import send_mail
from django.shortcuts import render
from phonenumbers import phonenumber
from django.db.models import Q
from rest_framework import generics
from .models import User
from .serializer import UserDetailsSerializer
from rest_framework.permissions import AND, AllowAny, IsAuthenticated
from pytube import YouTube
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

import pyautogui as pg
import time
import webbrowser

from rest_framework.response import Response

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)



# For Filter
from rest_framework.filters import SearchFilter
# Create your views here.

def home(request):
    return HttpResponse("<marquee><b>Software made by Pacis Jules ISHIMWE</b></marquee>")


class UserList(generics.ListCreateAPIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class=UserDetailsSerializer

    # Search
    filter_backends = [SearchFilter]
    search_fields = ['username']


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,context={'request': request})

        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)


        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'phone': user.phone,
            'type':user.type,
            'Created':created
        })




