from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def tiger(request):
    return render(request, 'tiger.html')

def peacock(request):
    return render(request, 'peacock.html')

def lotus(request):
    return render(request, 'lotus.html')

def mango(request):
    return render(request, 'mango.html')