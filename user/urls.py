from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='regsiter'),
    path('login/', views.loginn, name='login'),
]
