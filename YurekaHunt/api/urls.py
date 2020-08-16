from django.urls import path
from . import views 

urlpatterns = [
    path("", views.api_urls, name='api'),
    path("post-list/", views.post_list, name='task-list'),
    path("post-detail/<int:slug>/", views.detail_view, name='post-list'),

] 
