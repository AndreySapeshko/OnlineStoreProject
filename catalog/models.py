from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=100, verbose_name='Категория')
    description = models.CharField(max_length=300, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}: {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['name']


class Product(models.Model):

    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.CharField(max_length=300, verbose_name='Описание')
    product_image = models.ImageField(upload_to='images/', verbose_name='Фото продукта')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return f'{self.name} цена: {self.price} р.'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ['name']
