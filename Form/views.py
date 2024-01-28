from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def login_user(request):
    if request.user.is_authenticated == True:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('/')

    return render(request, 'Form/signin.html')


def register_user(request):
    if request.user.is_authenticated == True:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        User.objects.create_user(username=username, password=password1)
        return redirect('/')
    return render(request, 'Form/signup.html')


def logout_user(request):
    logout(request)
    return redirect('/')

