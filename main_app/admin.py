from django.contrib import admin
from .models import Record
# Register your models here.
#class SubmitAdmin(admin.ModelAdmin):
#    list_filter = ['staff','date']

#admin.site.register(SubmitAttendance, SubmitAdmin)
admin.site.register(Record)
