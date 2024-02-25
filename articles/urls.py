from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('<int:article_id>/', views.article_detail, name='article_detail'),
    path('<int:article_id>/edit', views.edit_article, name='edit_article'),
    path('', views.article_list, name='article_list'),

]