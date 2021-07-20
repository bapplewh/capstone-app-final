from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
    return render(request,'accounts/index.html')

def about(request):
    return render(request,'accounts/about.html')

def testimonials(request):
    return render(request,'accounts/testimonials.html')

def signup(request):
    return render(request,'accounts/signup.html')

def dashboard(request):
    orders = Order.objects.all()
    clients = Client.objects.all()

    context = {'orders': orders, 'clients': clients}

    return render(request,'accounts/dashboard.html', context)

def packages(request):
    packages = Package.objects.all()

    return render(request,'accounts/packages.html', {'packages': packages})

def client(request, pk_test):
    client = Client.objects.get(id=pk_test)
    orders = client.order_set.all()

    context = {'client': client, 'orders': orders}

    return render(request,'accounts/client.html', context)