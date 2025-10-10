from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def catalog(request):
    return render(request, 'catalog/catalog.html')


def home(request):
    latest_products = Product.objects.all().order_by('-created_at')[:5]
    return render(request, 'catalog/home.html', {'products': latest_products})


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        phone = request.POST.get('phone')
        print(f'Сообщение от {name} {phone}: {message}')
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, 'catalog/contacts.html')


def product(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {'product': product}
    return render(request, 'catalog/product.html', context)
