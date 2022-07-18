# Generated by Django 4.0.5 on 2022-07-11 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_cartitem_user_alter_cartitem_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon_code', models.CharField(max_length=10)),
                ('is_expired', models.BooleanField(default=False)),
                ('discount_price', models.IntegerField(default=100)),
                ('minimum_amount', models.IntegerField(default=500)),
            ],
        ),
    ]
