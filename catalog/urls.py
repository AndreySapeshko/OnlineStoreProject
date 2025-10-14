from django.urls import path
from catalog import views

app_name = 'catalog'

urlpatterns = [
    path('catalog/', views.catalog, name='catalog'),
    path('home/', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('product/<int:product_id>', views.product, name='product'),
    path('add_product/', views.add_product, name='add_product')
]