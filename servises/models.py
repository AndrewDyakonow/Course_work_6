from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name='ФИО')
    email = models.EmailField(verbose_name='Электронная почта')
    comment = models.CharField(max_length=255, verbose_name='Комментарий')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['name']
