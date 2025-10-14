from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView

from .models import Product, Category
from .forms import ProductForm


def home(request):
    products = Product.objects.all()
    return render(request, 'catalog/home.html', {'products': products})


# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         message = request.POST.get('message')
#         phone = request.POST.get('phone')
#         print(f'Сообщение от {name} {phone}: {message}')
#         return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
#     return render(request, 'catalog/contacts.html')


class ContactsView(View):
    def get(self, request):
        return render(request,'catalog/contacts.html')

    def post(self, request):
        name = request.POST.get('name')
        message = request.POST.get('message')
        phone = request.POST.get('phone')
        print(f'Сообщение от {name} {phone}: {message}')
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")



class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'description', 'product_image', 'price', 'category']
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'product_image', 'price', 'category']
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')



class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


# def product(request, product_id):
#     product = Product.objects.get(id=product_id)
#     context = {'product': product}
#     return render(request, 'catalog/product_detail.html', context)


def add_product(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
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
