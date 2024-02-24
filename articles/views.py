# In articles/views.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Article


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles': articles})


def show_base(request):
    return render(request, 'base.html', {})


def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    comments = article.comments.all()
    return render(request, 'article_detail.html', {
        'article': article,
        'comments': comments,
    })

