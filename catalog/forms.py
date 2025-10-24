import os

from django import forms
from django.conf import settings
from PIL import Image

from .models import Product, Category



class ProductForm(forms.ModelForm):
    """ Класс описывающий форму для регистрации и редактирования Product """

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'product_image', 'is_active']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def clean_product_image(self):
        """ Метод валидации изображения по формату, размеру, весу и представлению """

        image = self.cleaned_data.get('product_image')
        if not image:
            return image

        if image.size > settings.MAX_UPLOAD_SIZE:
            size_mb = image.size / 1024 / 1024
            max_mb = settings.MAX_UPLOAD_SIZE / 1024 / 1024
            raise forms.ValidationError(f'Размер файла не должен привышать {max_mb} МБ. Размер вашего файла: {size_mb:.1f} МБ.')

        ext = os.path.splitext(image.name)[1].lower()
        if ext not in settings.ALLOWED_IMAGE_EXTENSIONS:
            raise forms.ValidationError(
                f'Недопустимый формат файла. Разрешенные форматы: {", ".join(settings.ALLOWED_IMAGE_EXTENSIONS)}'
            )

        try:
            img = Image.open(image)
            img.verify()

            image.seek(0)
            img = Image.open(image)
            width, height = img.size

            if width > settings.MAX_IMAGE_WIDTH or height > settings.MAX_IMAGE_HEIGHT:
                raise forms.ValidationError(
                    f'Размер изображения не должен превышать {settings.MAX_IMAGE_WIDTH}x{settings.MAX_IMAGE_HEIGHT} пикселей'
                )

            image.seek(0)

        except (IOError, SyntaxError, AttributeError):
            raise forms.ValidationError('Файл поврежден или не является валидным изображением')

        return image


    def clean_price(self):
        """ Метод валидации поля цена, не должно быть отрицательным """

        price = self.cleaned_data.get('price')
        if price and price < 0:
            raise forms.ValidationError(message='Цена не может быть ниже ноля.')
        return price

    def clean(self):
        """ Метод валидации на содержание запрещенных слов """

        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        for word in settings.FORBIDDEN_WORDS:
            if name and description and (word in name.lower() or word in description.lower()):
                raise forms.ValidationError(f'Слово "{word}" нельзя использовать в названии и описании')
        return cleaned_data

    def __init__(self, *args, **kwargs):
        """ метод устанавливает стиль формы """

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
        self.fields['is_active'].widget.attrs.update({
            'class': 'form-check-input', 'placeholder': 'Опубликовать'
        })


class CategoryForm(forms.ModelForm):
    """ Класс описывающий форму создания и редактирования Category """

    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        """ Метод устанавливает стиль форме """

        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control', 'placeholder': 'Введите название'
        })
        self.fields['description'].widget.attrs.update({
            'class': 'form-control', 'placeholder': 'Введите описание Категории'
        })
