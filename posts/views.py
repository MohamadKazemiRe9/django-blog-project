from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

# Create your views here.

def blog_list(request):
    # articles = Article.objects.all()
    articles = Article.publish.all()
    return render(request, "blogs/list.html", {"articles":articles})