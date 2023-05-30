from django.urls import path
from .views import room, home, create_room

urlpatterns = [
    path('', home, name='chat'),
    path('<int:id>/', room, name='room'),
    path('add_room/', create_room, name='add_room'),
]