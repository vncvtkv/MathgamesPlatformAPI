from django.db import models

# Create your models here.

from django.contrib.auth import get_user_model
from core.models import BaseModel

User = get_user_model()


class Tag(models.Model):
    """Tags(genres) of posts"""

    title = models.CharField(max_length=256)
    description = models.TextField()
    slug = models.SlugField(
        max_length=64,
        unique=True,
    )

    def __str__(self):
        return self.title


class Post(BaseModel):
    """Posts by users"""

    title = models.CharField(max_length=256)
    text = models.TextField()

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    tag = models.ManyToManyField(
        Tag,
        related_name="post",
    )

    def __str__(self):
        return self.title


class Comment(BaseModel):
    """Comments to posts"""

    text = models.TextField()

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
