from django.contrib import admin
from .models import Record,Major,Chapter,Category,Article,Contact
# Register your models here.
#class SubmitAdmin(admin.ModelAdmin):
#    list_filter = ['staff','date']

#admin.site.register(SubmitAttendance, SubmitAdmin)
admin.site.register(Record)
admin.site.register(Major)
admin.site.register(Chapter)
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Contact)
