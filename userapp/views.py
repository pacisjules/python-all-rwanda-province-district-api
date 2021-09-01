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
from .models import User,Needjob
from .serializer import UserDetailsSerializer,Needjobserailizer
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



    #NeedJob view

class NeedjobList(generics.ListCreateAPIView):
        permission_classes = (AllowAny,)
        queryset = Needjob.objects.all()
        serializer_class= Needjobserailizer

class Detailneedjob(generics.RetrieveUpdateDestroyAPIView):
        permission_classes = (AllowAny,)
        queryset = Needjob.objects.all()
        serializer_class= Needjobserailizer



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



@csrf_exempt
def youtubedownloader(request):

    
    if request.method == 'POST':
        data = json.loads(request.body)
        video=data['link']
        yt = YouTube(video)

        info=[]
        audio=[]

        video=[
        {
            'Video Title':yt.title,
            'video_pic':yt.thumbnail_url,
        },
    ]
        for stream in yt.streams.filter(progressive=True):
            type=stream.mime_type
            res=stream.resolution

            links={
            'Type':type,
            'Resolution':res,
            'Link':stream.url
            }
            
            info.append(links)

        for sound in yt.streams.filter(only_audio=True):
            type=sound.mime_type
            res=sound.resolution

            links={
            'Type':type,
            'Resolution':res,
            'Link':stream.url
            }
            
            audio.append(links)
        
            
        #return HttpResponse(info, content_type='text/json')
        return JsonResponse({'Info':video,'Download_videos': info,'Download_audios': audio}, content_type='text/json')
        
    return JsonResponse({'data': 'This Api use POST request only'})







@csrf_exempt
def phone(request):

    if request.method == 'POST':
        data = json.loads(request.body)
        phone_number=data['phone']
        num1=data['num1']
        num2=data['num2']
        sum=num1+num2

        detectnumber=phonenumbers.parse(phone_number)
        location=geocoder.description_for_number(detectnumber, 'en')
        provider=carrier.name_for_number(detectnumber, 'en')

        information=[
        {
            'Phone number':phone_number,
            'Country location':location,
            'Provider':provider,
        },
        {
            'Message':'Api works well',
            'Sum of Numbers':sum
        }
    ]

        
        
        return JsonResponse({'Phone location access': information}, content_type='text/json')
        
    return JsonResponse({'data': 'This Api use POST request only'})


@csrf_exempt
def whatsapp(request):

    
    if request.method == 'POST':
        data = json.loads(request.body)
        phones=data['phones']
        message = data['txt_message']

        for x in phones:
            webbrowser.open_new('https://web.whatsapp.com/send?phone=+25'+x+'&text='+message)
            time.sleep(20)
            
            time.sleep(2)
            width, height = pg.size()
            pg.click(width / 2, height / 2)
            pg.press('enter')
            print('sent')
            
            time.sleep(13)
            pg.hotkey('ctrl', 'w')
            print('Closed') 

        
        #return HttpResponse(video, content_type='text/json')
        return JsonResponse({'Result': 'sent'}, content_type='text/json')
        
    return JsonResponse({'data': 'This Api use POST request only'})



