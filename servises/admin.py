from django.contrib import admin

from servises.models import Client, Settings


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