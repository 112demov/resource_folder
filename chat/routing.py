from django.urls import path

from . import consumer

websocket_urlpatterns = [
    path('ws/<int:id>/', consumer.ChatConsumer.as_asgi()),
]