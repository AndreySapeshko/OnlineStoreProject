from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView

from .models import Product, Category
from .forms import ProductForm, CategoryForm


# def home(request):
#     products = Product.objects.all()
#     return render(request, 'catalog/home.html', {'products': products})


class HomeView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'catalog/home.html', {'products': products})


class ContactsView(View):
    def get(self, request):
        return render(request,'catalog/contacts.html')

    def post(self, request):
        name = request.POST.get('name')
        message = request.POST.get('message')
        phone = request.POST.get('phone')
        print(f'Сообщение от {name} {phone}: {message}')
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")



class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')



class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    template_name = 'catalog/category_form.html'
    form_class = CategoryForm
    success_url = reverse_lazy('catalog:category_list')


class CategoryListView(ListView):
    model = Category
    template_name = 'catalog/category_list.html'
    context_object_name = 'categories'


class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category
    template_name = 'catalog/category_detail.html'
    context_object_name = 'category'


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    template_name = 'catalog/category_form.html'
    form_class = CategoryForm
    success_url = reverse_lazy('catalog:category_list')


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'catalog/category_confirm_delete.html'
    success_url = reverse_lazy('catalog:category_list')


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
