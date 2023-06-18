from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class product(models.Model):

    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to=None)

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)