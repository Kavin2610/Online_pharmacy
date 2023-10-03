# urls.py
app_name = 'cart'

from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart, name="cart"),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart_view'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
]
