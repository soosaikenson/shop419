from django.urls import path
from . import views # importing the views from the app to access the functions


urlpatterns = [
    path('login',views.Login.as_view(), name='signin'),
    path('register',views.UserRegister.as_view(), name='signup'),


]