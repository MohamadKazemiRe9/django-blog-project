from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Article(models.Model):
    STATUS_OF_ARTICLES = (
        ("checking", "Checking"),
        ("rejected", "Rejected"),
        ("published", "Published")
    )

    title = models.CharField(max_length=300)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Articles")
    status = models.CharField(max_length=12, choices=STATUS_OF_ARTICLES, default="checking")

    class Meta:
        ordering = ["-created"]
    
    def __str__(self) -> str:
        return f"{self.title} writed by {self.author}"