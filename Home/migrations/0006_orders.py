# Generated by Django 4.0.6 on 2022-08-16 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_rename_first_name_customer_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('cart', models.CharField(max_length=50)),
                ('customer', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, to='Home.customer')),
                ('product', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, to='Home.product')),
            ],
        ),
    ]
