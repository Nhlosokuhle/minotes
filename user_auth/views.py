from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirmpass']
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('user_auth:register')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken.')
            return redirect('user_auth:register')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already taken.')
            return redirect('user_auth:register')
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        auth_login(request, user)
        return redirect('minotes:home')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('minotes:home')
        else:
            messages.error(request, 'Invalid credentials.')
            return redirect('user_auth:login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return redirect('minotes:home')
