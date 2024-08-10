from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    ACCOUNT_TYPE = [
        ('personal', 'Personal'),
        ('wholesale', 'Wholesale'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPE, default='personal')

    def __str__(self):
        return f"{self.user.username}'s Profile"


    


