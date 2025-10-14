from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст сообщения')
    preview = models.ImageField(upload_to='blog/images/', verbose_name='Изображение')
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    count_views = models.IntegerField()
