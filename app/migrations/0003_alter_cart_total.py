# Generated by Django 4.2.3 on 2023-09-03 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_сustomer_cart_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.FloatField(blank=True, null=True),
        ),
    ]