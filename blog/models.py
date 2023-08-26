from django.conf import settings
from django.db import models
from django.utils.timezone import now

# Create your models here.
NULLABLE = {
    'blank': True,
    'null': True,
}


class Blog(models.Model):
    title = models.CharField(max_length=63, verbose_name='Заголовок')
    body = models.TextField(max_length=255, verbose_name='Тело')
    image = models.ImageField(upload_to='', default='fire.png', verbose_name='Картинка')
    view = models.SmallIntegerField(default=0, verbose_name='Просмотры')
    date = models.DateTimeField(default=now, verbose_name='Дата публикации')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name='автор'
    )
    is_active = models.BooleanField(default=True, verbose_name='Признак')

    def delete(self, using=None, keep_parents=False):
        self.is_active = False
        self.save()

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ['-date']

    def __str__(self):
        return f'{self.title}'
