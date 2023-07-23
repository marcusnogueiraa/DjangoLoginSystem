from django.shortcuts import render


def login_view(request):
    return render(request, 'accounts/pages/login.html')

def register_view(request):
    return render(request, 'accounts/pages/register.html')

# Create your views here.
