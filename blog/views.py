from django.http import Http404
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

class PostCreateView(CreateView):
    """ Класс описывающий представление страницы blog/post_form.html создание сообщения """

    model = Post
    fields = ['title', 'text', 'preview', 'is_published']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:post_list')


class PostListView(ListView):
    """ Класс описывающий представление страницы blog/post_list.html """

    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        """ Метод отбирает только опубликованные сообщения """

        return Post.objects.filter(is_published=True)


class PostDetailView(DetailView):
    """ Класс описывающий представление страницы blog/post_detail.html """

    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        """ Метод увеличивает счетчик просмотров при просмотре поста """

        obj = super().get_object(queryset)
        viewed_posts = self.request.session.get('viewed_posts', [])

        if obj.id not in viewed_posts:
            obj.count_views += 1
            obj.save()
            viewed_posts.append(obj.id)
            self.request.session['viewed_posts'] = viewed_posts
        return obj


class PostUpdateView(UpdateView):
    """ Класс описывающий представление страницы blog/post_form.html редактирование поста """

    model = Post
    fields = ['title', 'text', 'preview', 'is_published']
    template_name = 'blog/post_form.html'

    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs={'pk': self.object.pk})


class PostDeleteView(DeleteView):
    """ Класс описывающий представление страницы blog/post_confirm_delete.html удаление поста """

    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')
