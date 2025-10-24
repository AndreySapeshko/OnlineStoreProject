from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView

from .models import Product, Category
from .forms import ProductForm, CategoryForm


# def home(request):
#     products = Product.objects.all()
#     return render(request, 'catalog/home.html', {'products': products})


class HomeView(View):
    """ Класс описывающий представление страницы catalog/home.html """

    def get(self, request):
        products = Product.objects.all()
        return render(request, 'catalog/home.html', {'products': products})


class ContactsView(View):
    """ Класс описывающий представление страницы catalog/contacts.html """

    def get(self, request):
        """ Метод определяет поведение при get-запросе """

        return render(request,'catalog/contacts.html')

    def post(self, request):
        """ Метод определяет поведение при post-запросе """

        name = request.POST.get('name')
        message = request.POST.get('message')
        phone = request.POST.get('phone')
        print(f'Сообщение от {name} {phone}: {message}')
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")



class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """ Класс описывающий представление страницы catalog/product_confirm_delete.html удаление продукта """

    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')

    def post(self, request, product_pk):
        product = get_object_or_404(Product, product_pk)

        if not request.user.has_perm('catalog.can_delete_product'):
            return HttpResponseForbidden('У вас нет прав удалять продукты.')

        product.delete()
        return redirect('catalog:product_list')


class ProductListView(ListView):
    """ Класс описывающий представление страницы catalog/product_list.html """

    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """ Класс описывающий представление страницы catalog/product_form.html редактирование продукта """

    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

    def post(self, request, product_pk):
        product = get_object_or_404(Product, product_pk)

        if not request.user.has_perm('catalog.can_unpublish_product'):
            return HttpResponseForbidden('У вас нет прав отменять публикацию продукта.')

        product.delete()
        return redirect('catalog:product_list')


class ProductCreateView(LoginRequiredMixin, CreateView):
    """ Класс описывающий представление страницы catalog/product_form.html создание продукта """

    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')



class ProductDetailView(LoginRequiredMixin, DetailView):
    """ Класс описывающий представление страницы catalog/product_detail.html """

    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class CategoryCreateView(LoginRequiredMixin, CreateView):
    """ Класс описывающий представление страницы catalog/category_form.html создание категории """

    model = Category
    template_name = 'catalog/category_form.html'
    form_class = CategoryForm
    success_url = reverse_lazy('catalog:category_list')


class CategoryListView(ListView):
    """ Класс описывающий представление страницы catalog/category_list.html """

    model = Category
    template_name = 'catalog/category_list.html'
    context_object_name = 'categories'


class CategoryDetailView(LoginRequiredMixin, DetailView):
    """ Класс описывающий представление страницы catalog/category_detail.html """

    model = Category
    template_name = 'catalog/category_detail.html'
    context_object_name = 'category'


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    """ Класс описывающий представление страницы catalog/category_form.html редактирование категории """

    model = Category
    template_name = 'catalog/category_form.html'
    form_class = CategoryForm
    success_url = reverse_lazy('catalog:category_list')


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    """ Класс описывающий представление страницы catalog/category_confirm_delete.html удаление категории """

    model = Category
    template_name = 'catalog/category_confirm_delete.html'
    success_url = reverse_lazy('catalog:category_list')
