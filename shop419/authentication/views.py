from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic import CreateView

# importing django.contrib.auth usercreation forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.views import LoginView


# Create your views here.

class UserRegister(CreateView):
    form_class = UserCreationForm  # specifying the way in which the form object should be built
    template_name = 'register.html'
    success_url = reverse_lazy('signin') # url name to redirect to once signup is done

class Login(LoginView):
    template_name = "login.html"