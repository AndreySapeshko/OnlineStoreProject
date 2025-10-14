from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'text', 'preview', 'is_published', 'count_views']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:post_list')


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'text', 'preview', 'is_published', 'count_views']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:post_list')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')
