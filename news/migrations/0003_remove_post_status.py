# Generated by Django 5.0.6 on 2024-08-04 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_post_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='status',
        ),
    ]
