from django.contrib import admin

from sauth.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('username', 'language', 'date_joined')
    list_filter = ('language', )
