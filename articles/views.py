# In articles/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm
from jalali_date import datetime2jalali, date2jalali
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from django.http import JsonResponse


def article_list(request):
    articles = Article.objects.order_by('-created_at')
    return render(request, 'article_list.html', {'articles': articles})


# views.py

def update_likes(request):
    if request.method == 'POST':
        article_id = request.POST.get('article_id')
        article = get_object_or_404(Article, pk=article_id)
        article.likes += 1
        article.save()
        print("something cool")
        return JsonResponse({'likes': article.likes})
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)


def delete_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.user == article.author:
        if request.method == 'POST':
            article.delete()
            return redirect('home')  # Redirect to the home page after deletion
        else:
            # Render delete confirmation template (optional)
            return render(request, 'delete_article_confirmation.html', {'article': article})
    else:
        return redirect('article_detail', article_id=article_id)


def edit_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.user == article.author:
        if request.method == 'POST':
            # Handle form submission
            title = request.POST.get('title')
            content = request.POST.get('content')
            # Update article object
            article.title = title
            article.content = content
            article.save()
            return redirect('article_detail', article_id=article_id)
        else:
            # Render edit article template
            return render(request, 'edit_article.html', {'article': article})
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

@login_required
def create_comment(request, article_id):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            article = get_object_or_404(Article, pk=article_id)
            comment = Comment.objects.create(author=request.user, article=article, content=content)
            return redirect('article_detail', article_id=article_id)
    return redirect('article_detail', article_id=article_id)  # Redirect back to article detail page if comment creation fails

