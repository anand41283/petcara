from django.contrib import messages,auth
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
from pet_app.forms import CustomerRegister


def home(request):
    return render(request, 'home.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin_home')
            elif user.is_officer:
                return redirect('officer_home')
            elif user is not None and user.is_user:
                if user.status == True:
                    login(request, user)
                    return redirect('user_home')
                else:
                    messages.info(request, 'You are not Approved to login')

        else:
            messages.info(request, 'INVALID CREDENTIALS')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login_view')


def customer_register(request):
    form = CustomerRegister()
    if request.method == 'POST':
        form = CustomerRegister(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_user = True
            user.save()
            messages.info(request, 'Customer Registered Successful')
            return redirect('login_view')
    return render(request, 'customer_register.html', {'form': form})
