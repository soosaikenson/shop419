from django.shortcuts import render
from .models import Product

from django.urls import reverse_lazy

# to help load the template files
from django.template import loader

# to help return an http response to the user for any given request
from django.http import HttpResponse

# importing the genereic class based views for CRUD operations
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView




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



# Create
class AddProduct(CreateView):
    model = Product
    fields = ['name', 'price', 'desc', 'pic', 'stock']
    template_name = 'addProduct.html'
    success_url = reverse_lazy('home')

# Read
class ProductDetails(DetailView):
    model = Product
    template_name = 'prod_details.html'
    context_object_name = 'prod'

# Update
from django.urls import reverse

class UpdateProduct(UpdateView):
    model = Product
    fields = '__all__'
    template_name = 'editProduct.html'

    def get_success_url(self):
        return reverse('prod_details', kwargs = {'pk' : self.object.pk})
    
# Delete 
class DeleteProduct(DeleteView):
    model = Product
    template_name = 'delProduct.html'
    success_url = reverse_lazy('home')