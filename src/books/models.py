from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=120)
    category = models.CharField(max_length=50)
    tags = models.TextField(max_length=120)
    discription = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=0, max_digits=10000)
    img = models.ImageField(upload_to='image/', null=True)