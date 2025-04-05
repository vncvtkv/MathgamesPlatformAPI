from rest_framework import viewsets 
from django.shortcuts import get_object_or_404
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import OwnerOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (OwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.none()
    serializer_class = CommentSerializer
    permission_classes = (OwnerOrReadOnly,)

    def get_queryset(self):
        id = self.kwargs["post_id"]
        post = get_object_or_404(Post, id=id)
        return Comment.objects.filter(post=post)

    def perform_create(self, serializer):
        id = self.kwargs["post_id"]
        post = get_object_or_404(Post, id=id)
        serializer.save(author=self.request.user, post=post)