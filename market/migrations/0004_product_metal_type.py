# Generated by Django 5.0.6 on 2024-08-06 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_product_remove_currentmetalprice_rhodium_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='metal_type',
            field=models.CharField(choices=[('gold', 'Gold'), ('silver', 'Silver'), ('platinum', 'Platinum'), ('palladium', 'Palladium')], default='gold', max_length=10),
        ),
    ]
