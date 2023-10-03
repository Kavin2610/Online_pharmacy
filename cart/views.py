

# Create your views here.
# views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import  Cart, CartItem, Item

def add_to_cart(request, product_id):
    product = get_object_or_404(Item, id=product_id)
    
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, Item=product, quantity = 1)
    print(cart_item.Item)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return render(request, 'cart.html', {'cart_items': [cart_item]})

def cart_view(request):
    user_cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=user_cart)
    return render(request, 'cart.html', {'cart_items': cart_items})

def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()
    return redirect('cart.html')

def cart(request):
    return render(request, 'cart.html')
