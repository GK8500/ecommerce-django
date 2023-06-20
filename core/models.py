from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):

    name = models.CharField(max_length=50, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    desc = models.TextField(null=True)
    image = models.ImageField(upload_to=None, null= True)

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

