from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'market/home.html')

def products(request):
    return render(request, 'market/products.html')

def busket(request):
    return render(request, 'market/busket.html')