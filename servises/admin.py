from django.contrib import admin

from servises.models import Client, Settings, Messages, Logs


# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'email', 'comment', 'is_active')


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = (
        'mailing_name',

        'date_mailing',
        'date_end_mailing',
        'periodicity',
        'status',
        'is_active',
    )
    filter_horizontal = ('client_name',)


@admin.register(Messages)
class MessagesAdmin(admin.ModelAdmin):
    list_display = ('theme', 'body', 'is_active')


@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_last', 'status', 'answer')
