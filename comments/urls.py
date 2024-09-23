from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r"add-post", PostViewSet, basename="posts")
router.register(r"threads-comments", ThreadViewSet, basename="threads")
urlpatterns = [
    path("api/v1/", include(router.urls)),
]