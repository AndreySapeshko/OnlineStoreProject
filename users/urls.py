from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from catalog.urls import app_name
from users.views import RegisterView, UserUpdateView, UserDetailView

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html', next_page='catalog:home'), name='login'),
    path('logout/', LogoutView.as_view(next_page='catalog:home'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('user/edit/', UserUpdateView.as_view(), name='user_edit'),
    path('user/', UserDetailView.as_view(), name='user_detail')
]
