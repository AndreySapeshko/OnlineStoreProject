from django.urls import path
from catalog import views

app_name = 'catalog'

urlpatterns = [
    path('catalog/', views.catalog, name='catalog'),
    path('home/', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('product/', views.product, name='product')
]