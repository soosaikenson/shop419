from django.urls import path
from . import views # importing the views from the myapp to access the functions

from . views import homeView, aboutView, AddProduct, ProductDetails, UpdateProduct, DeleteProduct

urlpatterns = [
    path('', views.homeView, name='home'),
    path("about", views.aboutView, name="aboutpage"),
    path("products", views.ProductList.as_view(), name="products"),

    path('products/add', AddProduct.as_view(), name='add_prod'),
    path('products/<int:pk>', ProductDetails.as_view(), name='prod_details'),     # dynamic urlpattern
    path('products/edit/<int:pk>', UpdateProduct.as_view(), name='edit_prod'),
    path('products/del/<int:pk>', DeleteProduct.as_view(), name='del_prod')
]