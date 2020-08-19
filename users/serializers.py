from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.contrib.auth import get_user_model 
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import LoginSerializer
# Serializers define the API representation.
from rest_framework.permissions import IsAuthenticated

class CustomRegisterSerializer(RegisterSerializer):
    # email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
    email = None

class CustomLoginSerializer(LoginSerializer):
    # email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
    email = None


class ListAllUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ['url', 'username',]

class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = get_user_model()
        # fields = ['url', 'username', 'email','date_joined',]
        fields = ['url', 'username',]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']