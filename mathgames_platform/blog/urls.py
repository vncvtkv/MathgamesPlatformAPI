from django.urls import path, include

from rest_framework.routers import DefaultRouter

from blog.views import PostViewSet

router = DefaultRouter() 

router.register('post', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
