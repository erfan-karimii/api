from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User


class PostSerilizers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields="__all__"


class UserSerilizers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields="__all__"