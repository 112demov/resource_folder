from email import message
import json

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from django.contrib.auth.models import User
from .models import Message, Room

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.id = self.scope['url_route']['kwargs']['id']
        self.room_group_name = 'chat_%s' % self.id

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        room = data['room']
        date = data['date']

        await self.save_message(username, room, message, date)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
                'room': room,
                'date': date
            }

        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        room = event['room']
        date = event['date']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'room': room,
            'date': date
        }))

    @sync_to_async
    def get_user(self, username):
        return User.objects.filter(username=username).first()
    
    @sync_to_async
    def save_message(self, username, room, message, date):
        user = User.objects.get(username=username)
        room = Room.objects.get(id=room)

        Message.objects.create(user=user, room=room, msg=message, date=date)