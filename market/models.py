from django.db import models

# Create your models here.


# A model where the current and historical prices are stored
class CurrentMetalPrice(models.Model):
    date = models.DateField(auto_now_add=True)
    gold_price = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)
    silver_price = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)
    platinum_price = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)
    palladium_price = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)

    def __str__(self):
        return f"Metal prices for {self.date}"
    


# A model that helps display the relevant information about a selected product
class Product(models.Model):

    METALS = [
        ('gold', 'Gold'),
        ('silver', 'Silver'),
        ('platinum', 'Platinum'),
        ('palladium', 'Palladium'),
    ]



    name = models.CharField(max_length=255)
    blurb = models.TextField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    weight = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    country_of_origin = models.CharField(max_length=100)
    density = models.CharField(max_length=100)
    melting_range = models.CharField(max_length=100)
    metal_type = models.CharField(max_length=10, choices=METALS, default='gold')

    def __str__(self):
        return self.name