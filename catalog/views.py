from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.context_processors import request
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.cache import cache
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView
from unicodedata import category

from .models import Product, Category
from .forms import ProductForm, CategoryForm
from .services import ProductService


# def home(request):
#     products = Product.objects.all()
#     return render(request, 'catalog/home.html', {'products': products})


class HomeView(View):
    """ Класс описывающий представление страницы catalog/home.html """

    def get(self, request):
        products = Product.objects.all()
        return render(request, 'catalog/home.html', {'products': products})


class ProductsInCategoryView(ListView):
    """ Класс описывающий представление страницы catalog/category_products.html """

    model = Product
    template_name = 'catalog/category_products.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_pk = self.kwargs['pk']
        context['category'] = Category.objects.get(pk=category_pk)
        context['products'] = ProductService.get_products_in_category(category_pk)
        return context



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



class ProductDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    """ Класс описывающий представление страницы catalog/product_confirm_delete.html удаление продукта """

    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')

    def test_func(self):
        """ Проверяет, является ли пользователь владельцем продукта или модератором """

        product = self.get_object()
        user = self.request.user
        return user == product.owner or user.has_perm('catalog.can_delete_product')


class ProductListView(ListView):
    """ Класс описывающий представление страницы catalog/product_list.html """

    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = cache.get('products_queryset')
        if not queryset:
            queryset = super().get_queryset()
            cache.set('products_queryset', queryset, 60*15)
        return queryset


class ProductUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    """ Класс описывающий представление страницы catalog/product_form.html редактирование продукта """

    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

    def test_func(self):
        """ Проверяет, является ли пользователь владельцем продукта или модератором """
        product = self.get_object()
        user = self.request.user
        return user == product.owner or user.has_perm('catalog.can_unpublish_product')


class ProductCreateView(LoginRequiredMixin, CreateView):
    """ Класс описывающий представление страницы catalog/product_form.html создание продукта """

    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        """Автоматически устанавливаем владельца при создании"""

        if not form.instance.owner_id:
            form.instance.owner = self.request.user
        return super().form_valid(form)


@method_decorator(cache_page(60*15), name='dispatch')
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
