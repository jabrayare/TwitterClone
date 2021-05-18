from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(
                    'Username exists. Please choose another username.')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,
                                   'User exists. Please choose another username.')
                    return redirect('register')
                else:
                    messages.success(
                        request, 'account created Successfully!')
                    user = User.objects.create_user(
                        first_name=first_name, last_name=last_name, email=email, username=username, password=password)
                    user.save()
                    auth.login(request, user)
                    return redirect('create_profile')
        else:
            messages.error(request, 'Passwords DO NOT match!')
            return redirect('register')

    return render(request, 'account/register.html', {})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            messages.success(request, 'You are logged in.')
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password is Wrong!')
            return redirect('login')
    return render(request, 'account/login.html', {})


def logout(request):
    auth.logout(request)
    return redirect('login')
