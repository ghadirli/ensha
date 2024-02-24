from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from articles.models import Article

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

@login_required
def acc_article_list(request):
    article_ids = [1, 2, 3]  # Example list of IDs
    articles = Article.objects.filter(pk__in=article_ids)
    
    return render(request, 'acc_article_list.html', {'articles': articles})

