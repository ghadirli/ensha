# In articles/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm


def article_list(request):
    articles = Article.objects.order_by('-created_at')
    return render(request, 'article_list.html', {'articles': articles})


def edit_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.user == article.author:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('article_detail', article_id=article_id)
        else:
            form = ArticleForm(instance=article)
        return render(request, 'edit_article.html', {'form': form})
    else:
        return redirect('article_detail', article_id=article_id)

def show_base(request):
    return render(request, 'base.html', {})


def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    comments = article.comments.all()
    return render(request, 'article_detail.html', {
        'article': article,
        'comments': comments,
    })

