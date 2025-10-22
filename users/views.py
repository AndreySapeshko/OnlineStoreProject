import os

from django.contrib.auth.models import User
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from dotenv import load_dotenv
from django.contrib.auth import login
from django.core.mail import send_mail
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, UserUpdateForm
from .models import CustomUser


class RegisterView(CreateView):
    """ Класс описывающий представление страницы users/register.html """

    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('catalog:home')

    def send_welcome_email(self, user_email):
        """ Метод отправляющий новому пользователю приветствие """

        subject = 'Добро пожаловать в наш магазин'
        message = 'Спасибо, что зарегистрировались у нас!'
        from_email = os.getenv('YANDEX_EMAIL')
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)

    def form_valid(self, form):
        """ Метод проводит валидацию данных введенных в форму """

        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    """ Класс описывающий представление страницы users/user_form.html редактирования профиля """

    model = CustomUser
    form_class = UserUpdateForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('users:user_detail')

    def get_object(self, queryset=None):
        return self.request.user


class UserDetailView(DetailView):
    """ Класс описывающий представление страницы users/user_detail.html """

    model = CustomUser
    template_name = 'users/user_detail.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.request.user
