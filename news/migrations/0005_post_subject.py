# Generated by Django 5.0.6 on 2024-08-11 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_subscriber'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subject',
            field=models.CharField(default='news', max_length=100),
        ),
    ]
