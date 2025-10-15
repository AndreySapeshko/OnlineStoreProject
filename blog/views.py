from django.http import Http404
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

    def get_queryset(self):
        return Post.objects.filter(is_published=True)


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        obj = super().object(queryset)
        if not obj.is_active:
            raise Http404("Object not found")
        obj.count_views += 1
        return obj


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'text', 'preview', 'is_published', 'count_views']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:post_detail')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')
