from django.db import models
from django.urls import reverse
from django.utils.timezone import now

NULLABLE = {
    'blank': True,
    'null': True,
}


class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name='ФИО')
    email = models.EmailField(verbose_name='Электронная почта')
    comment = models.CharField(max_length=255, verbose_name='Комментарий')

    is_active = models.BooleanField(default=True, verbose_name='Активность')

    def get_absolute_url(self):
        return reverse('servises:client', args=[self.pk])

    def delete(self, **kwargs):
        self.is_active = False
        self.save()

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['name']

    def __str__(self):
        return f'{self.name}, {self.email}, {self.comment}, {self.is_active}'


class Settings(models.Model):

    class Periodicity(models.TextChoices):
        EVERY_MINUTES = 'Раз в минуту', 'Раз в минуту'
        EVERY_DAY = 'Раз в день', 'Раз в день'
        EVERY_WEEK = 'Раз в неделю', 'Раз в неделю'
        EVERY_MONTH = 'Раз в месяц', 'Раз в месяц'

    class Status(models.TextChoices):
        CREATED = 'Создана', 'Создана'
        ACTIVE = 'Активна', 'Активна'
        ENDING = 'Завершена', 'Завершена'

    mailing_name = models.CharField(max_length=127, verbose_name='Название')
    message = models.ForeignKey('Messages', on_delete=models.CASCADE, verbose_name='Письмо для рассылки', **NULLABLE)
    client_name = models.ManyToManyField(Client, verbose_name='Имя клиентов')
    date_mailing = models.DateTimeField(default=now, verbose_name='Дата начала рассылки')
    date_end_mailing = models.DateTimeField(default=now, verbose_name='Дата окончания рассылки')
    is_active = models.BooleanField(default=True, verbose_name='Активность')
    periodicity = models.CharField(
        max_length=63,
        choices=Periodicity.choices,
        default=Periodicity.EVERY_DAY,
        verbose_name='Периодичность рассылки'
    )
    status = models.CharField(
        max_length=63,
        choices=Status.choices,
        default=Status.CREATED,
        verbose_name='Статус рассылки'
    )

    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'

    def delete(self, **kwargs):
        self.is_active = False
        self.save()

    def get_absolute_url(self):
        return reverse('servises:setting_detail', args=[self.pk])

    def __str__(self):
        return f'{self.mailing_name}, {self.message}, {self.client_name}, {self.date_mailing}, ' \
               f'{self.date_end_mailing}, {self.is_active}, {self.periodicity}, {self.status}'


class Messages(models.Model):
    theme = models.CharField(max_length=63, verbose_name='Тема письма')
    body = models.TextField(max_length=511, verbose_name='Содержимое письма')
    is_active = models.BooleanField(default=True, verbose_name='Активность')

    def delete(self, **kwargs):
        self.is_active = False
        self.save()

    def __str__(self):
        return f'{self.theme}, {self.body}'

    class Meta:
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'
        ordering = ['theme']


class Logs(models.Model):
    title = models.CharField(max_length=63, default=str(now), verbose_name='Название')
    date_last = models.DateTimeField(**NULLABLE, verbose_name='Дата последней попытки')
    status = models.CharField(max_length=25, verbose_name='Статус попытки')
    answer = models.TextField(max_length=511, default=None, verbose_name='Ответ сервера')

    def __str__(self):
        return f'{self.date_last}, {self.status}, {self.answer}'

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'
