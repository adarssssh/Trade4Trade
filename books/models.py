from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=120)
    category = models.CharField(max_length=50, null=True, blank=True)
    tags = models.TextField(max_length=120, null=True, blank=True)
    discription = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=0, max_digits=10000, null=True, blank=True)
    img = models.ImageField(upload_to='images/', null=True)