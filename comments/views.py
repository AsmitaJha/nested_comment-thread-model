from django.shortcuts import render
from rest_framework import viewsets
from .models import Post, Thread
from .serializers import PostSerializer, ThreadSerializer

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    #Model viewset allows CRUD (Create, Read, Update, and Delete) operations
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    
class ThreadViewSet(viewsets.ModelViewSet):
    queryset=Thread.objects.all()
    serializer_class=ThreadSerializer
    
    #overriding the 'perform_create' method of viewset to save the comment requested by a user
    def perform_create(self,serializer):
       serializer.save(user=self.request.user)