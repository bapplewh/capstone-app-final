from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'accounts/dashboard.html')

def packages(request):
    return render(request,'accounts/packages.html')

def clients(request):
    return render(request,'accounts/clients.html')