from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.blog.views import PostViewSet, CommentViewSet

router = DefaultRouter() 
router.register(r'post', PostViewSet)
router.register(r'post/(?P<post_id>[1-9][0-9]*)/comment', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
