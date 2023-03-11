from django.db import models

# Create your models here.

class Subscribers(models.Model):
    
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    amount = models.IntegerField()
    
   