from django.shortcuts import render
from .models import Product

# to help load the template files
from django.template import loader

# to help return an http response to the user for any given request
from django.http import HttpResponse

from django.views.generic import ListView, CreateView, UpdateView, DeleteView


# Create your views here.

def homeView(request):
    products = Product.objects.all()   # its like select * from Product

    # Creating a context dictionary to be used to render the template with info
    context = {
        'product_list' : products, # the key we create here will be available in template design in home.html

        'current_page' : 'home'
    }
    template = loader.get_template("home.html")
    return HttpResponse(template.render(context, request))

def aboutView(request):

    context = {
        'current_page' : 'about',
        "name" : "Kenson",
        "students" : ["Deepak","Surya","Dattatri"],

       'slept' : True

    }
    template=loader.get_template("about.html")
    return HttpResponse(template.render(context, request))

class ProductList(ListView):
    model = Product
    template_name = 'products.html'