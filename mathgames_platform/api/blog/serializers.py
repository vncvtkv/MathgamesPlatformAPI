from rest_framework import serializers

from .models import Post, Comment, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('title',)


class PostSerializer(serializers.ModelSerializer):
    """Serializes Post data for API responses.
 
    Includes:
    - Read-only `author` field (username)
    - Nested comments and tags
    """
    author = serializers.StringRelatedField(read_only=True)
    tag = TagSerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = ('id', 'title', 'text', 'tag', 'author')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ('text', 'author', 'post')
