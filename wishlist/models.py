from django.db import models
from accounts .models import Account
from store .models import Product

# Create your models here.
class Wishlist(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    def get_url(self):
        return reverse('products_by_category',args=[self.slug])


    def __str__(self):
        return self.product
