from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import SignUpView


urlpatterns = [
    path('', views.acc_article_list, name='acc_article_list'),
    path("signup/", SignUpView.as_view(), name="signup"),
    path('create/', views.create_article, name='acc_article_list'),
]