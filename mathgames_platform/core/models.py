from django.db import models

# Create your models here.


class BaseModel(models.Model):
    """Abstract model"""

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ('-created_at',)
        abstract = True