from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Blog(models.Model):
    """Represents an overall blog."""
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    """Represents an individual blog post."""
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name="posts"
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
