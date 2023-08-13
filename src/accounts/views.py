from django.shortcuts import render


def login_view(request):
    return render(request, 'accounts/pages/login.html', status=200)

def register_view(request):
    return render(request, 'accounts/pages/register.html', status=200)

def sucess_view(request):
    return render(request, 'accounts/pages/sucess.html', status=200)

# Create your views here.
