# Generated by Django 5.0.6 on 2024-08-05 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentMetalPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('gold', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('silver', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('platinum', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('palladium', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('rhodium', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
            ],
        ),
    ]
