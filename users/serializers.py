from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import LoginSerializer
# Serializers define the API representation.
from rest_framework.permissions import IsAuthenticated
# from rest_framework.renderers import JSONRenderer

class CustomRegisterSerializer(RegisterSerializer):
    """
    Custom User Registeration Serializer Inhereting from rest_auth RegisterSerializer
    """
    # email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
    email = None


class CustomLoginSerializer(LoginSerializer):
    """
    Custom User Login Serializer Inhereting from rest_auth LoginSerializer
    
    """
    # renderer_classes = [JSONRenderer]
    # email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
    email = None


class ListAllUserSerializer(serializers.ModelSerializer):
    '''
    Show all users list
    '''
    class Meta:
        model = get_user_model()
        fields = ['id','username', 'date_joined']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Show user attached with a url"""

    class Meta:
        model = get_user_model()
        # fields = ['url', 'username', 'email','date_joined',]
        fields = ['url', 'username', ]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """ Show Group attached with a url"""
    class Meta:
        model = Group
        fields = ['url', 'name']
