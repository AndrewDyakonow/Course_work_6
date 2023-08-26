# Generated by Django 4.2.3 on 2023-07-19 11:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('servises', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logs',
            name='title',
            field=models.CharField(default='<function now at 0x7fbef8e5fa60>', max_length=63, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='messages',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='создатель'),
        ),
    ]
