from django.shortcuts import render, redirect
from .utils import *
from .forms import *


menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Отзывы', 'url_name': 'comment'},
        ]

def index(request):
    product = Product.objects.all()
    type = ProductType.objects.all()
    context = {
        'product': product,
        'type': type,
        'menu': menu,
        'title': 'Главная страница',
        'type_selected': 0,
    }
    return render(request, 'Salon/Product.html', context=context)


def about(request):
    return render(request, 'Salon/about.html', {'menu': menu, 'title': 'О нас'})


def comment(request):
    return render(request, 'Salon/Comment.html', {'menu': menu, 'title': 'Комментарии'})


def show_type_product(request, type_id, product_id=None):
    product = Product.objects.filter(product_type=type_id)
    type = ProductType.objects.all()
    cart_items = CartItem.objects.filter(user=request.user)
    context = {
        'product': product,
        'type': type,
        'menu': menu,
        'title': 'Отображение по категориям ',
        'type_selected': type_id,
        'cart_items': cart_items,
    }
    return render(request, 'Salon/Product.html', context=context)






