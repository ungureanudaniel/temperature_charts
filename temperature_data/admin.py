from django.contrib import admin
from .models import Device
#, DataInput

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
# class DataInputAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'devices', 'temp', 'date', 'time')
#     list_filter = ('devices', 'date',)
#
admin.site.register(Device, DeviceAdmin)
# admin.site.register(DataInput, DataInputAdmin)
