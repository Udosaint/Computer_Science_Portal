from django.shortcuts import render, redirect

# Create your views here.

def adminLogin(request):
    return render(request, 'office/index.html'); 


def Dashboard(request):
    return render(request, 'office/home.html'); 