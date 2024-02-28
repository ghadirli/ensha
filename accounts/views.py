from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from articles.models import Article

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from venues.models import Venue


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


@login_required
def acc_article_list(request):
    article_ids = [1, 2, 3]  # Example list of IDs
    articles = Article.objects.filter(pk__in=article_ids)

    return render(request, 'acc_article_list.html', {'articles': articles})


def join_leave_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    if request.method == 'POST':
        if request.user in venue.members.all():
            venue.members.remove(request.user)
        else:
            venue.members.add(request.user)
        return redirect('venue_detail', venue_id=venue_id)
    return render(request, 'join_leave_venue.html', {'venue': venue})


@login_required
def create_article(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.user
        venue_ids = request.POST.getlist('venues')
        new_article = Article.objects.create(title=title, content=content, author=author)
        new_article.venues.add(*venue_ids)
        return redirect('article_detail', article_id=new_article.id)
        # Process form data and create new article
        # Remember to associate the article with the logged-in user
        # Redirect to article detail view or article list view
    else:
        venues = Venue.objects.all()
        return render(request, 'create_article.html', {'venues': venues})
