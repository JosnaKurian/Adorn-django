# Generated by Django 4.0.5 on 2022-07-11 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0006_cartitem_coupon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='coupon',
        ),
        migrations.DeleteModel(
            name='Coupon',
        ),
    ]