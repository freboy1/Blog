from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse

# Create your views here.
def register(request):

    form = UserCreationForm()
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')


    context = {'form': form}

    return render(request, 'user/register.html', context)

def loginn(request):
    form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'user/login.html', context)