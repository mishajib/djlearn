from django.db import models


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length = 125)
    email = models.EmailField()
    address = models.TextField(max_length = 255)
    city = models.CharField(max_length = 150)
    zipcode = models.CharField(max_length = 15)
