from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('<int:article_id>/', views.article_detail, name='article_detail'),
    path('<int:article_id>/edit', views.edit_article, name='edit_article'),
    path('', views.article_list, name='article_list'),
    path('<int:article_id>/delete', views.delete_article, name='delete_article'),
    path('update_likes/', views.update_likes, name='update_likes'),
    path('<int:article_id>/create_comment', views.create_comment, name='create_comment'),
]