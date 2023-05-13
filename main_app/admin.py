from django.contrib import admin

from .models import Record, Major, Chapter, Category, Article, Contact, OtherRecord, Like


admin.site.register(Record)
admin.site.register(Major)
admin.site.register(Chapter)
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Contact)
admin.site.register(OtherRecord)
admin.site.register(Like)
