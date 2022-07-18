from django.db import models
from store.models import Product
from accounts.models import Account

# Create your models here.

class Cart(models.Model):
    cart_id    = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id



# class Coupon(models.Model):
#     coupon_code = models.CharField(max_length = 10)
#     is_expired = models.BooleanField(default=False)
#     discount_price = models.IntegerField(default=100)
#     minimum_amount = models.IntegerField(default=500)


class CartItem(models.Model):
    user     = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart     = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    # coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField()
    is_active=models.BooleanField(default=True)

    def sub_total(self):
        return self.product.price * self.quantity

    def __unicode__(self):
        return self.product