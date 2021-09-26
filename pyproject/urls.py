from django import urls
from django.contrib import admin
from django.urls import path, include
from userapp.views import UserList, CustomAuthToken, home


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [

    path('', home),

    path('api/', include('rwanda_treegovmap.urls')),


    path('users', UserList.as_view(), name="user"),
    path('admin/', admin.site.urls),

    path('customLogin', CustomAuthToken.as_view(), name="user"),
    #path('auth/register', Registrationuser.as_view(), name='UserRegister'),

    path('auth/login', TokenObtainPairView.as_view(), name='Userlogin'),
    path('auth/token-refresh', TokenRefreshView.as_view(), name='Usertokenrefresh'),
]
