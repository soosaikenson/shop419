from django.db import models

# Create your models here.
# Automatic ORM(Object Relational Mapping) methods are already pre-designed in this class

class Product(models.Model):
    # list out all the object variables below and initialize with certain classes.
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(null=False)
    desc = models.TextField()
    pic  = models.ImageField(upload_to="products/", null=False)
    stock = models.PositiveBigIntegerField(default=1)