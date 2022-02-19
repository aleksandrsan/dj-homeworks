from django.shortcuts import render, redirect
from .models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):

    sort_order_param = request.GET.get('sort', 'name')

    Phone.objects.all()
    if sort_order_param == 'name':
        sort_order ='name'
    elif sort_order_param == 'min_price':
        sort_order ='price'
    else:
        sort_order ='-price'

    phone_objects = Phone.objects.order_by(sort_order)

    template = 'catalog.html'
    context = {
        'phones': phone_objects,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)
