from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст сообщения')
    preview = models.ImageField(upload_to='blog/images/', verbose_name='Изображение')
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    count_views = models.IntegerField()

    def __str__(self):
        return f'{self.created_at} {self.title}'

    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'записи'
        ordering = ['created_at']
