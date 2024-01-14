

# Create your models here.
# models.py
from django.contrib.auth.models import User

from item.models import Item
from django.db import models
from django.conf import settings


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    Item = models.ForeignKey(Item, null="False", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    @property
    def total_price(self):
        return self.Item.price * self.quantity
    def item_image(self):
        return self.Item.image


    class Meta:
        unique_together = ('cart', 'Item')

class checkout(models.Model):
    cartitem_id = models.ForeignKey(CartItem, on_delete=models.CASCADE)
    cartid = models.ForeignKey(Cart, on_delete=models.CASCADE)
    total_price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

class checkoutdetails(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    postalcode = models.CharField(max_length=7)
    city = models.CharField(max_length=20)
    phoneNumber = models.CharField(max_length=12)
    country =models.CharField(max_length=20, default="India")
    

    
    
