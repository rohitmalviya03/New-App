# Generated by Django 4.0.6 on 2022-08-16 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0007_remove_orders_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='price',
            field=models.CharField(default=0, max_length=50),
        ),
    ]