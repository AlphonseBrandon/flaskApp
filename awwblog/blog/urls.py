from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name = 'blog'

URLPattern = [
    path('', views.post_list, name="post_list"),
    path('<slug:post>/', views.post_detail, name="post_detail"),
]