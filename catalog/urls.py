from django.urls import path
from catalog import views
from catalog.admin import Product
from catalog.views import ProductDeleteView, ProductListView, ProductCreateView, ProductUpdateView, ProductDetailView, \
    ContactsView

app_name = 'catalog'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('product/new/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/product_edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('product/<int:pk>/product_delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('add_product/', views.add_product, name='add_product')
]