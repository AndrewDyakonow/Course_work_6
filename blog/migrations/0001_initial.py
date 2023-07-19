# Generated by Django 4.2.3 on 2023-07-19 20:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_created=django.utils.timezone.now, verbose_name='Дата публикации')),
                ('title', models.CharField(max_length=63, verbose_name='Заголовок')),
                ('body', models.TextField(max_length=255, verbose_name='Тело')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Аватар')),
                ('view', models.SmallIntegerField(default=0, verbose_name='Просмотры')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='автор')),
            ],
            options={
                'verbose_name': 'Запись',
                'verbose_name_plural': 'Записи',
                'ordering': ['-date'],
            },
        ),
    ]
