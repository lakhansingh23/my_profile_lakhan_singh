from django.db import models
class contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    Comments=models.TextField(max_length=200)
    
# Create your models here.
