# Generated by Django 3.1.5 on 2021-06-04 04:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_product_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tags',
        ),
    ]
