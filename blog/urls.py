from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/<int:id>/', views.blog, name='blog'),
    path('blog/add/', views.blog_add, name='blog_add'),
    path('blog/delete/<int:id>/', views.blog_delete, name='blog_delete'),
]
