from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request, 'user/register.html')

def loginn(request):
    return HttpResponse('Login Here')