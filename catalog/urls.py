from django.urls import path
from catalog import views
from catalog.admin import Product
from catalog.views import ProductDeleteView, ProductListView, ProductCreateView, ProductUpdateView, ProductDetailView, \
    ContactsView, HomeView, CategoryCreateView, CategoryListView, CategoryDetailView, CategoryUpdateView, \
    CategoryDeleteView, ProductsInCategoryView

app_name = 'catalog'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('product/new/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/product_edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('product/<int:pk>/product_delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('category/new/', CategoryCreateView.as_view(), name='category_create'),
    path('category_list/', CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('category/<int:pk>/category_edit/', CategoryUpdateView.as_view(), name='category_edit'),
    path('category/<int:pk>/category_delete/', CategoryDeleteView.as_view(), name='category_delete'),
    path('category/<int:pk>/products/', ProductsInCategoryView.as_view(), name='category_products')
]