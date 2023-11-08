from django.shortcuts import render
from .models import Article

def articles(request):
    articles = Article.objects.all()
    return render(request, 'Articles/articles.html', {'articles': articles})