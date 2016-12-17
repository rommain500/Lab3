from django.contrib import admin

from hotel.models import Picture
from hotel.models import Hotel
from hotel.models import Reserve


@admin.register(Picture)
class PicAdmin(admin.ModelAdmin):
    list_display = ('path', )


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    filter_horizontal = ('pictures', )


@admin.register(Reserve)
class ReserveAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'client', 'date_start', 'date_end', 'person_amount')
    list_filter = ('date_start', 'date_end')
