# Generated by Django 4.2.3 on 2023-07-19 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата публикации'),
        ),
    ]
