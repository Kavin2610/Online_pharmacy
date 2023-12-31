from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Prescription(models.Model):
    patient_name = models.CharField(max_length=255)
    prescription_images = models.ImageField(upload_to='prescription_images', null=True, blank=True )
    prescription_pdf = models.FileField(upload_to='prescription_pdf', null=True, blank=True)

    #def __str__(self):
       #return self.patient_name

class Rating(models.Model):
    RATE_CHOICES = [
        ('1', 'one'),
        ('2', 'two'),
        ('3', 'three'),
        ('4', 'four'),
        ('5', 'five'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    score = models.CharField(max_length=10, choices=RATE_CHOICES)
    comment = models.TextField(null=True, blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)


