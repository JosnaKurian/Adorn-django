# Generated by Django 4.0.5 on 2022-07-12 04:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_payment_razor_pay_order_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='razor_pay_payment_id',
        ),
    ]
