from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'url', 'description', 'technologies', 'image', 'date_posted', 'user']

        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'image', 'bio',]
