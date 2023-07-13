from django.contrib import admin

from servises.models import Client


# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'comment')
