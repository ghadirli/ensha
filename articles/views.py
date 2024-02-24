# In articles/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Article


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles': articles})


def show_base(request):
    return render(request, 'base.html', {})

@login_required
def create_article(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.user

        new_article = Article.objects.create(title=title, content=content, author=author)
        return redirect('article_detail', article_id=new_article.id)
        # Process form data and create new article
        # Remember to associate the article with the logged-in user
        # Redirect to article detail view or article list view
    else:
        return render(request, 'create_article.html')


def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    comments = article.comments.all()
    return render(request, 'article_detail.html', {
        'article': article,
        'comments': comments,
    })

