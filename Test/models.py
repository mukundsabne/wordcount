from django.db import models

# Create your models here.

class Test(models.Model):
    name=models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    mobileno = models.IntegerField(max_length=10)
    
