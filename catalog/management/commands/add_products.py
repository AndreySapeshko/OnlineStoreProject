import json

from pathlib import Path
from django.core.management.base import BaseCommand
from django.core.management import call_command
from decimal import Decimal

from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Load test data from fixture'

    def handle(self, *args, **kwargs):
        # Удаляем все записи
        Product.objects.all().delete()
        Category.objects.all().delete()
        # Получаем данные из файла
        json_file = Path(__file__).parent.parent.parent.parent / 'catalog_fixture.json'
        if Path.exists(json_file):
            with open(json_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
        # Создаем списки категорий и продуктов
        categories = []
        products = []
        for element in data:
            if element.get('model') == 'catalog.category':
                category = {
                    'name': element.get('fields').get('name'),
                    'description': element.get('fields').get('description')
                }
                categories.append(category)
            if element.get('model') == 'catalog.product':
                product = {
                    'name': element.get('fields').get('name'),
                    'description': element.get('fields').get('description'),
                    'product_image': element.get('fields').get('product_image'),
                    'price': Decimal(element.get('fields').get('price')),
                    'category': element.get('fields').get('category')
                }
                products.append(product)
        print(products)
        # Записываем категории
        for category in categories:
            category, created = Category.objects.get_or_create(**category)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully added category: {category.name}'))
            else:
                self.stdout.write(
                    self.style.WARNING(f'Student already exists: {category.name}'))
        # Создаем объекты категорий
        smartphones, _ = Category.objects.get_or_create(name='Смартфоны')
        televisor, _ = Category.objects.get_or_create(name='Телевизоры')
        # Запись продуктов
        for product in products:
            # Заменяем у продуктов номер категории на объект
            if product.get('category') == 1:
                product['category'] = smartphones
            elif product.get('category') == 2:
                product['category'] = televisor
            # Записываем в базу продукты
            product, created = Product.objects.get_or_create(**product)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully added product: {product.name}'))
            else:
                self.stdout.write(
                    self.style.WARNING(f'Student already exists: {product.name}'))

        # А можно было сделать все гораздо проще
        # call_command('loaddata', 'catalog_fixture.json')
        # self.stdout.write(self.style.SUCCESS('Successfully loaded data from fixture'))
