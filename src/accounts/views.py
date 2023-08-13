from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser

def login_view(request):
    return render(request, 'accounts/pages/login.html', status=200)

def register_view(request):
    return render(request, 'accounts/pages/register.html', status=200)

@login_required(login_url='/login')
def sucess_view(request):
    return render(request, 'accounts/pages/sucess.html', status=200)

def user_register(request):
    if  request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = CustomUser.objects.create_user(username=username, email=email, password=password)
        login(request, user)

        return redirect('accounts:login_view')
    return render(request, 'accounts/pages/register.html', status=200)

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            #TODO: Change the redirect function param to home url
            return redirect('accounts:sucess_view')
        else:
            return render(request, 'accounts/pages/login.html', status=200)


