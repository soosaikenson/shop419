from django.urls import path
from . import views # importing the views from the myapp to access the functions

urlpatterns = [
    path('', views.homeView, name='home'),
    path("about", views.aboutView, name="aboutpage"),
    path("products", views.ProductList.as_view(), name="products")
]