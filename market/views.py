from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'market/home.html')

def about(request):
    return render (request, 'market/about.html')

def product(request):
    return render (request, 'market/product.html')
