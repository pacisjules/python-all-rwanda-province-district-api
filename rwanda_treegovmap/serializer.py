from rest_framework import serializers
from .models import occupation_type,leader,provinces,district,sector,cell,district_gallery



#1. occupation Type Serializer
class occupation_type_serializer(serializers.ModelSerializer):

        created_by = serializers.ReadOnlyField(source='created_by.username')
        class Meta:
            fields = (
                'id',
                'type_name',
                'type',
                'reg_date',
                'reg_time',
                'created_by',
            )
            model = occupation_type

#2. leader Serializer
class leader_serializer(serializers.ModelSerializer):
    
        created_by = serializers.ReadOnlyField(source='created_by.username')
        image = serializers.ImageField(max_length=None, use_url=True)

        class Meta:
            fields = (
                'id',
                'names',
                'phone_number',
                'leader_for',
                'occ_type',
                'image',
                'reg_date',
                'reg_time',
                'created_by',
            )
            model = leader

#3. province Serializer
class province_serializer(serializers.ModelSerializer):
    
        created_by = serializers.ReadOnlyField(source='created_by.username')

        class Meta:
            fields = (
                'id',
                'name',
                'leader',
                'surface',
                'reg_date',
                'reg_time',
                'created_by',
            )
            model = provinces


#4. district Serializer
class district_serializer(serializers.ModelSerializer):
    
        created_by = serializers.ReadOnlyField(source='created_by.username')

        class Meta:
            fields = (
                'id',
                'name',
                'province',
                'popularity',
                'leader',
                'reg_date',
                'reg_time',
                'created_by',
            )
            model = district

#5. sector Serializer
class sector_serializer(serializers.ModelSerializer):
    
        created_by = serializers.ReadOnlyField(source='created_by.username')

        class Meta:
            fields = (
                'id',
                'name',
                'province',
                'district',
                'leader',
                'reg_date',
                'reg_time',
                'created_by',
            )
            model = sector

#6. cell Serializer
class cell_serializer(serializers.ModelSerializer):
    
        created_by = serializers.ReadOnlyField(source='created_by.username')

        class Meta:
            fields = (
                'id',
                'name',
                'province',
                'district',
                'sector',
                'leader',
                'reg_date',
                'reg_time',
                'created_by',
            )
            model = cell

#7. District Gallery Serializer
class district_gallery_serializer(serializers.ModelSerializer):
    
        created_by = serializers.ReadOnlyField(source='created_by.username')
        image = serializers.ImageField(max_length=None, use_url=True)

        class Meta:
            fields = (
                'id',
                'name',
                'province',
                'district',
                'image',
                'reg_date',
                'reg_time',
                'created_by',
            )
            model = district_gallery