from django import forms
from django.conf import settings

from .models import Product, Category



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'product_image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price and price < 0:
            raise forms.ValidationError(message='Цена не может быть ниже ноля.')
        return price

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        for word in settings.FORBIDDEN_WORDS:
            if name and description and (word in name.lower() or word in description.lower()):
                raise forms.ValidationError(f'Слово "{word}" нельзя использовать в названии и описании')
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control', 'placeholder': 'Введите название'
        })
        self.fields['description'].widget.attrs.update({
            'class': 'form-control', 'placeholder': 'Введите описание продукта'
        })
        self.fields['price'].widget.attrs.update({
            'class': 'form-control', 'placeholder': 'Введите цену'
        })
        self.fields['category'].widget.attrs.update({
            'class': 'form-control', 'placeholder': 'Выберите категорию'
        })
        self.fields['product_image'].widget.attrs.update({
            'class': 'form-control', 'placeholder': 'Вставьте изображение'
        })


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control', 'placeholder': 'Введите название'
        })
        self.fields['description'].widget.attrs.update({
            'class': 'form-control', 'placeholder': 'Введите описание Категории'
        })
