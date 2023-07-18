from django.contrib import admin

from users.models import Users


# Register your models here.
@admin.register(Users)
class AdminUsers(admin.ModelAdmin):
    list_display = ('email', 'first_name')
