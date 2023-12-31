

# Create your views here.
# views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import  Cart, CartItem, Item, checkout
from .forms import CheckoutForm


def add_to_cart(request, product_id):
    product = get_object_or_404(Item, id=product_id)
    
    cart, created = Cart.objects.get_or_create(user=request.user)
    item_exists = CartItem.objects.filter(Item=product).exists()
    if item_exists:
        cart_item = CartItem.objects.get(Item=product)
        cart_item.quantity += 1
    else:
        cart_item, created = CartItem.objects.get_or_create(cart=cart, Item=product, quantity = 1)
    print(cart_item.Item)
    #if not created:
    #cart_item.quantity += 1
    cart_item.save()
    print("item saved successfully")
    return render(request, 'cart.html', {'cart_items': [cart_item]})

def cart_view(request):
    user_cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=user_cart)
    #total_price_item = cart_items * Item.quantity 
    print('cart_items' ,cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items})


def remove_from_cart(request, product_id):
    cart = Cart.objects.get(user=request.user)  
    product = get_object_or_404(Item, id=product_id)
    cart_item = get_object_or_404(CartItem, cart=cart, Item=product)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return render(request, 'cart.html', {'cart_items': [cart_item]})
def cart(request):
    return render(request, 'cart.html')

def Checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('checkout.html')
    else:
        form = CheckoutForm()
    return render(request, 'checkout.html', {'form' : form})



def submit(request):
    return render(request, 'paymentportal.html')