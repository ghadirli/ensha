from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('create/', views.create_venue, name='create_venue'),
    path('list/', views.venue_list, name='venue_list'),
    path('<int:venue_id>/', views.venue_detail, name='venue_detail'),

]