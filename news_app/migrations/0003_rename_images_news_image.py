# Generated by Django 4.0 on 2023-06-08 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0002_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='images',
            new_name='image',
        ),
    ]
