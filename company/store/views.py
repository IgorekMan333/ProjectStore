from django.shortcuts import render, redirect
from .forms import CreateUserForm, OrderForm, CustomerForm
from .models import Product, Customer, Order
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if request.user.is_authenticated:
        return redirect ('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.info(request, 'Already exists')
                return redirect('home')
        return render(request, 'register.html', {'form': form})


def log(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            username = request.POST.get('username')
            password1 = request.POST.get('password1')
            user = authenticate(request, username=username, password=password1)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Password or username incorrect')
        return render(request, 'login.html', {'form': form})


def logoutUser(request):
    logout(request)
    return redirect('log')


@login_required(login_url='log')
def navbar(request):
    return render(request, 'navbar.html')


@login_required(login_url='log')
def base(request):
    return render(request, 'base.html')


@login_required(login_url='log')
def products(request):
    items = Product.objects.all()
    return render(request, 'products.html', {'items': items})


@login_required(login_url='log')
def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all().select_related('product', 'customer')
    order_count = orders.count()
    context = {
        'customers': customers,
        'orders': orders,
        'order_count': order_count,
    }
    return render(request, 'home.html', context)


@login_required(login_url='log')
def customer(request, pk):
    unit = Customer.objects.get(id=pk)
    orders = unit.order_set.all().select_related('product')
    order_count = orders.count()

    context = {
        'customer': unit,
        'orders': orders,
        'order_count': order_count
    }
    return render(request, 'customer.html', context)


@login_required(login_url='log')
def create_order(request, pk):
    unit = Customer.objects.get(id=pk)
    form = OrderForm(initial={'customer': unit})
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form,
    }
    return render(request, 'order_form.html', context)


@login_required(login_url='log')
def buyProduct(request, pk):
    product = Product.objects.get(id=pk)
    form = OrderForm(initial={'product': product})
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'order_form.html', context)


@login_required(login_url='log')
def update_order(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form,
    }
    return render(request, 'order_form.html', context)


@login_required(login_url='log')
def delete_order(request, pk):
    order = Order.objects.select_related('product').get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('home')
    context = {
        'item': order
    }
    return render(request, 'delete_order.html', context)


def create_customer(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form,
    }
    return render(request, "create_customer.html", context)





@login_required(login_url='log')
def userPage(request):
    return render(request, 'user.html')

