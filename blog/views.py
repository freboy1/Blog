from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Blog
from .forms import BlogForm
# Create your views here.
@login_required(login_url='user:login')
def home(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blog/home.html', context)

def blog(request, id):
    blogs = Blog.objects.get(id=id)
    form = BlogForm(instance=blogs)
    context = {'form': form}
    return render(request, 'blog/blog.html', context)

def blog_add(request):
    form = BlogForm()

    if request.method == 'POST':
        form = BlogForm(request.POST)
        form.user = request.user

        if form.is_valid():
            form.save()
            return redirect('home')


    context = {'form': form}
    return render(request, 'blog/blog_add.html', context)