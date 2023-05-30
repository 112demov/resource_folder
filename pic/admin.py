from django.contrib import admin
from .models import Picture


class AdminPicture(admin.ModelAdmin):
    list_display = ['img', 'title', 'alt', 'date']

admin.site.register(Picture, AdminPicture)
