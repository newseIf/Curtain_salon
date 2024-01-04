from django.shortcuts import render, redirect
from Salon.models import Product, CartItem
from .forms import *


def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'total_price': total_price})

def del_to_cart(request, product_id):
    product = Product.objects.get(product_id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product,
                                                        user=request.user)
    cart_item.quantity -= 1
    cart_item.save()
    return redirect('cart:view_cart')

def add_to_cart(request, product_id):
    product = Product.objects.get(product_id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product,
                                                        user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart:view_cart')




def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('cart:view_cart')

