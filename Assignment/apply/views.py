from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'apply/login.html')

def details(request):
    return render(request, 'apply/details.html')