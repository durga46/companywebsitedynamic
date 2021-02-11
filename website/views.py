from django.shortcuts import render

from .models import Product

from .models import People

# Create your views here.

def home(request):
    context = {}
    return render(request, 'website/home.html', context)

def products(request):
    context = {}

    context["products"] = Product.objects.all();

    return render(request, 'website/products.html', context)    

def people(request):
    context = {}

    context["peoples"] = People.objects.all();

    return render(request, 'website/people.html', context)  

def contactus(request):
    context = {}
    return render(request, 'website/contactus.html', context)  

        



