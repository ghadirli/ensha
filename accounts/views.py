from django.shortcuts import render
from django.contrib.auth.decorators import login_required
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
    articles = Article.objects.all()
    return render(request, 'acc_article_list.html', {'articles': articles})

