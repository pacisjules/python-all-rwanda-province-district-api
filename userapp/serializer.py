from rest_framework import serializers
from .models import User,Needjob
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer






class UserDetailsSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name',
                  'last_name','type', 'address','phone', 'city', 'about_me', 'password')

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserDetailsSerializer, self).create(validated_data)


class Needjobserailizer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'first_name',
            'last_name',
            'age',
        )
        
        model = Needjob