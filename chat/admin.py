from django.contrib import admin
from .models import Message, Room

admin.site.register(Message)

class RoomAdmin(admin.ModelAdmin):
    list_display = ('first_user', 'second_user', 'id')

    def save_model(self, request, obj, form, change):
        if not obj.first_user:
            obj.first_user = request.user
        obj.save()
admin.site.register(Room, RoomAdmin)
