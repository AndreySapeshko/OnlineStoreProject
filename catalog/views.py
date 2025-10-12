from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Category
from .forms import ProductForm

# Create your views here.
def catalog(request):
    return render(request, 'catalog/catalog.html')


def home(request):
    products = Product.objects.all()
    return render(request, 'catalog/home.html', {'products': products})


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


def add_product(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            product = form.save()
            return redirect('catalog:product', product_id=product.pk)
        else:
            # Вывод всех ошибок в консоль
            print("Форма невалидна!")
            print("Ошибки формы:", form.errors)
            print("Ошибки по полям:")
            for field in form:
                if field.errors:
                    print(f"Поле '{field.label}': {field.errors}")
    else:
        form = ProductForm()

    return render(request, 'catalog/add_product.html', {'form': form, 'categories': categories})
