from rest_framework import serializers
from .models import Thread, Post

class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields="__all__"
        
class ThreadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Thread
        exclude=["user"]