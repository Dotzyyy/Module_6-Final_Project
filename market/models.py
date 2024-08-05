from django.db import models

# Create your models here.

class CurrentMetalPrice(models.Model):
    date = models.DateField(auto_now_add=True)
    gold_price = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)
    silver_price = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)
    platinum_price = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)
    palladium_price = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)

    def __str__(self):
        return f"Metal prices for {self.date}"
    

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    image = models.ImageField(upload_to='products/')
    weight = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    country_of_origin = models.CharField(max_length=100)
    density = models.CharField(max_length=100)
    melting_range = models.CharField(max_length=100)

    def __str__(self):
        return self.name