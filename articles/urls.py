from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('create/', views.create_article, name='article_list'),
    path('<int:article_id>/', views.article_detail, name='article_detail'),
    path('', views.article_list, name='article_list'),
    path('base', views.show_base, name='base'),

]