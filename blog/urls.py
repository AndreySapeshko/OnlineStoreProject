from django.urls import path
from blog import views
from blog.views import PostListView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView

app_name = 'blog'

urlpatterns = [
    path('post_list/', PostListView.as_view(), name='post_list'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/post_edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/post_delete/', PostDeleteView.as_view(), name='post_delete')
]
