from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.loginn, name='login'),
    path('logout/', views.my_logout, name='logout'),
]
