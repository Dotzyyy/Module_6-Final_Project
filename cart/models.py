from django.db import models
from django.contrib.auth.models import User
from market.models import Product
# Create your models here.


#Model to help display the relevant item in a users cart
class CheckoutItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    weight = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.weight}g x {self.product.name}' 

    @classmethod
    def clear_cart(cls, user):
        """Clear all items in the cart for the given user."""
        cls.objects.filter(user=user).delete()