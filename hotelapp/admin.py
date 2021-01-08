from django.contrib import admin
from .models import *
# Register your models here.

class RoomAdmins(admin.ModelAdmin):
    list_display = ['number','category','beds','capacity']

class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'room','check_in', 'check_out']


admin.site.register(Room,RoomAdmins)
admin.site.register(Booking,BookingAdmin)