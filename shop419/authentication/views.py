from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic import CreateView

# importing django.contrib.auth usercreation forms


# Create your views here.

class UserRegister(CreateView):

    template_name = 'register.html'
    success_url = reverse_lazy('signin')
