

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
    Item = models.ForeignKey(Item, null='False',on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    
