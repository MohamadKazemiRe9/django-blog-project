from turtle import title
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
from datetime import datetime
from django.urls import reverse

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status="published")

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
    slug = models.SlugField(unique=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            now = datetime.now()
            self.slug = slugify(self.title)+"-"+str(now.year)+"-"+str(now.month)+"-"+str(now.day)
            self.save()

    class Meta:
        ordering = ["-created"]
    
    def __str__(self) -> str:
        return f"{self.title} writed by {self.author}"
    
    def get_absolute_url(self):
        return reverse("blogs:blog_detail", kwargs={"slug": self.slug})
    

    objects = models.Manager()
    publish = PublishedManager()