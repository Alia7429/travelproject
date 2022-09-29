from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.messages.storage import session
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template.context_processors import request


def login(request):
    if request.method == 'POST':
        u = request.POST['username']
        v = request.POST['password']
        user = auth.authenticate(username=u, password=v)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid")
            return redirect('login')
    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        x = request.POST['username']
        a = request.POST['first_name']
        b = request.POST['last_name']
        c = request.POST['email']
        d = request.POST['password']
        e = request.POST['password1']

        if d == e:
            if User.objects.filter(username=x):
                messages.info(request, "username taken")
                return redirect('register')
            elif User.objects.filter(email=c):
                messages.info(request, "email taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=x, first_name=a, last_name=b, email=c, password=d)
                user.save();
                return redirect('login')

        else:
            messages.info(request, "password not match")
            return redirect('register')

        return redirect('/')
    return render(request, "register.html", )


def logout(request:{session}):
    auth.logout(request)
    return redirect('/')
