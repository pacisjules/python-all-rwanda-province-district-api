from rest_framework import settings
from django.urls import path


#For file Upload
from django.conf.urls.static import static
from django.conf import settings #For Settings
#End For file Upload

from .views import *

urlpatterns = [    
    
    #1. Occupation
    path('occupations', ListOccupation.as_view(), name='Occupations'),
    path('occupations/<int:pk>', DetailOccupation.as_view(), name='Occupation detail'),

    #2. Leader
    path('leaders', ListLeaders.as_view(), name='Leaders'),
    path('leaders/<int:pk>', DetailLeader.as_view(), name='Leader detail'),

    #3. Province
    path('provinces', ListProvince.as_view(), name='Provinces'),
    path('provinces/<int:pk>', DetailProvince.as_view(), name='Province detail'),

    #4. District
    path('districts', ListDistricts.as_view(), name='districts'),
    path('districts/<int:pk>', DetailDistrict.as_view(), name='districts detail'),

    #5. Sector
    path('sectors', ListSectors.as_view(), name='sectors'),
    path('sectors/<int:pk>', DetailSectors.as_view(), name='sectors detail'),

    #6. Cell
    path('cells', ListCells.as_view(), name='cells'),
    path('cells/<int:pk>', DetailCell.as_view(), name='cells detail'),

    #7. District Gallery
    path('gallery', ListGallery.as_view(), name='Gallery'),
    path('gallery/<int:pk>', DetailGallery.as_view(), name='Gallery detail'),    

] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#For media File