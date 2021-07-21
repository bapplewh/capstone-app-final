from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import *
from .forms import ClientForm, OrderForm, CreateUserForm


# Create your views here.

def home(request):
    return render(request,'accounts/index.html')

def about(request):
    return render(request,'accounts/about.html')

def testimonials(request):
    return render(request,'accounts/testimonials.html')

def signup(request):
    return render(request,'accounts/signup.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect ('signin')

        context = {'form': form}

        return render(request,'accounts/register.html', context)

def signin(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username =request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')

            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}

        return render(request,'accounts/signin.html', context)


def logoutUser(request):
    logout(request)
    return redirect('signin')


@login_required(login_url='signin')
def dashboard(request):
    orders = Order.objects.all()
    clients = Client.objects.all()

    context = {'orders': orders, 'clients': clients}

    return render(request,'accounts/dashboard.html', context)


@login_required(login_url='signin')
def packages(request):
    packages = Package.objects.all()

    return render(request,'accounts/packages.html', {'packages': packages})


@login_required(login_url='signin')
def client(request, pk_test):
    client = Client.objects.get(id=pk_test)
    orders = client.order_set.all()

    context = {'client': client, 'orders': orders}

    return render(request,'accounts/client.html', context)


@login_required(login_url='signin')
def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form': form}

    return render (request, 'accounts/order-form.html', context)


@login_required(login_url='signin')
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


@login_required(login_url='signin')
def createClient(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form': form}

    return render (request, 'accounts/client-form.html', context)


@login_required(login_url='signin')
def deleteClient(request, pk):
    client = Client.objects.get(id=pk)
    if request.method == "POST":
        client.delete()
        return redirect('dashboard')

    context = {'item': client}

    return render(request, 'accounts/delete-client.html', context)