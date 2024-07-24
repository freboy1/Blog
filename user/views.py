from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def register(request):
    return render(request, 'user/register.html')

def loginn(request):
    form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'user/login.html', context)