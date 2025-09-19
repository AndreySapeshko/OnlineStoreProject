from django.urls import path
from catalog import views

urlpatterns = [
    path('catalog/', views.catalog, name='catalog'),
    path('home/', views.home, name='home'),
]