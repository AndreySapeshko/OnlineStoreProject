from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import CustomUser


class BaseUserForm:
    """ Родительский класс с общим для многих форм методом добавляющем стили форме """

    def __init__(self, *args, **kwargs):
        """ Метод добавляет стили форме """

        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class CustomUserCreationForm(BaseUserForm, UserCreationForm):
    """ Класс описывающий форму регистрации нового пользователя """

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['email', 'username', 'avatar', 'phone_number', 'country']


class UserUpdateForm(BaseUserForm, forms.ModelForm):
    """ Класс описывающий форму редактирования профиля пользователя """

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'avatar', 'phone_number', 'country']
