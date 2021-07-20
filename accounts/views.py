from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import ClientForm, OrderForm

# Create your views here.

def home(request):
    return render(request,'accounts/index.html')

def about(request):
    return render(request,'accounts/about.html')

def testimonials(request):
    return render(request,'accounts/testimonials.html')

def signup(request):
    return render(request,'accounts/signup.html')

def signin(request):
    return render(request,'accounts/signin.html')

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

def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form': form}

    return render (request, 'accounts/order-form.html', context)

def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form': form}

    return render(request, 'accounts/order-form.html', context)


def createClient(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form': form}

    return render (request, 'accounts/client-form.html', context)

def deleteClient(request, pk):
    client = Client.objects.get(id=pk)
    if request.method == "POST":
        client.delete()
        return redirect('dashboard')

    context = {'item': client}

    return render(request, 'accounts/delete-client.html', context)