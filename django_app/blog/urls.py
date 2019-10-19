from django.urls import path

from . import views
from .views import (
    home,
    detail, 
    create,
    update,
    delete,
    user_post
    )

app_name = 'blog'

urlpatterns = [
    path('', home, name='blog-home'),
    path('about', views.about, name='blog-about'),
    path('post/new', create, name='blog-create'),
    path('user/<str:username>', user_post, name='user-post'),    
    path('post/<int:pk>/detail', detail, name='blog-detail'),
    path('post/<int:pk>/update', update, name='blog-update'),
    path('post/<int:pk>/delete', delete, name='blog-delete'),
]
