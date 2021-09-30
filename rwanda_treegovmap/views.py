from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from rest_framework.permissions import AllowAny, IsAuthenticated
# For Filter
from rest_framework.filters import SearchFilter
# Create your views here.
from .models import *
from .serializer import *

# Create your views here.


#1. Occupation Views
class ListOccupation(generics.ListCreateAPIView):
    permission_classes = (
        permissions.AllowAny,
        )
    queryset = occupation_type.objects.all()
    serializer_class = occupation_type_serializer

    # Search
    filter_backends = [SearchFilter]
    search_fields = ['type_name','type']


class DetailOccupation(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = occupation_type.objects.all()
    serializer_class = occupation_type_serializer


#2. Leader Views
class ListLeaders(generics.ListCreateAPIView):
    permission_classes = (
        permissions.AllowAny,
        )
    queryset = leader.objects.all()
    serializer_class = leader_serializer

    # Search
    filter_backends = [SearchFilter]
    search_fields = ['names','leader_for','occ_type','phone_number']


class DetailLeader(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = leader.objects.all()
    serializer_class = leader_serializer


#3. Province Views
class ListProvince(generics.ListCreateAPIView):
    permission_classes = (
        permissions.AllowAny,
        )
    queryset = provinces.objects.all()
    serializer_class = province_serializer

    # Search
    filter_backends = [SearchFilter]
    search_fields = ['name','leader']


class DetailProvince(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = provinces.objects.all()
    serializer_class = province_serializer



#4. District Views
class ListDistricts(generics.ListCreateAPIView):
    permission_classes = (
        permissions.AllowAny,
        )
        
    queryset = district.objects.all()
    serializer_class = district_serializer

    # Search
    filter_backends = [SearchFilter]
    search_fields = ['name','leader']


class DetailDistrict(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = district.objects.all()
    serializer_class = district_serializer


#5. Sector Views
class ListSectors(generics.ListCreateAPIView):
    permission_classes = (
        permissions.AllowAny,
        )
    queryset = sector.objects.all()
    serializer_class = sector_serializer

    # Search
    filter_backends = [SearchFilter]
    search_fields = ['name','leader']


class DetailSectors(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = sector.objects.all()
    serializer_class = sector_serializer


#6. Cell Views
class ListCells(generics.ListCreateAPIView):
    permission_classes = (
        permissions.AllowAny,
        )
    queryset = cell.objects.all()
    serializer_class = cell_serializer

    # Search
    filter_backends = [SearchFilter]
    search_fields = ['name','leader']


class DetailCell(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = cell.objects.all()
    serializer_class = cell_serializer

#7. District Gallery Views
class ListGallery(generics.ListCreateAPIView):
    permission_classes = (
        permissions.AllowAny,
        )
    queryset = district_gallery.objects.all()
    serializer_class = district_gallery_serializer

    # Search
    filter_backends = [SearchFilter]
    search_fields = ['province','district']


class DetailGallery(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = district_gallery.objects.all()
    serializer_class = district_gallery_serializer


