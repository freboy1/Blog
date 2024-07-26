from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Blog

# Create your views here.
@login_required(login_url='user:login')
def home(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blog/home.html', context)

def blog(request, id):
    blogs = Blog.objects.filter(id=id)
    context = {'blogs': blogs}
    return render(request, 'blog/blog.html', context)
