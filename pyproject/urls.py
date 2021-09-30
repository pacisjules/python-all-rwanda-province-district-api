from django import urls
from django.contrib import admin
from django.urls import path, include
from userapp.views import UserList, CustomAuthToken, home

#For file Upload
from django.conf.urls.static import static
from django.conf import settings #For Settings
#End For file Upload



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
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #For media File
