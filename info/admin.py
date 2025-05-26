from django.contrib import admin
from .models import news_table,comments,ads,news_letter,addcategory

admin.site.register(news_table)
admin.site.register(comments)
admin.site.register(ads)
admin.site.register(news_letter)
admin.site.register(addcategory)