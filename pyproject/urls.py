from django import urls
from django.contrib import admin
from django.urls import path, include
from userapp.views import UserList, youtubedownloader,whatsapp, phone, CustomAuthToken, NeedjobList, Detailneedjob


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [

    path('needjob', NeedjobList.as_view(), name="list of needed job"),
    path('needjob/<int:pk>', Detailneedjob.as_view(), name='single'),

    path('youtube', youtubedownloader),
    path('phone', phone),
    path('whatsappApi', whatsapp),

    path('user/v1', UserList.as_view(), name="user"),
    path('admin/', admin.site.urls),

    path('customLogin', CustomAuthToken.as_view(), name="user"),
    #path('auth/register', Registrationuser.as_view(), name='UserRegister'),

    path('auth/login', TokenObtainPairView.as_view(), name='Userlogin'),
    path('auth/token-refresh', TokenRefreshView.as_view(), name='Usertokenrefresh'),
]
