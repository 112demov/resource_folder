from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Room(models.Model):
    room_image = models.ImageField(upload_to='images/', default='default_room_image.png')
    first_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='first_user')
    second_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='second_user')

    def get_absolute_url(self):
        return reverse('room', args=[str(self.id)])


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    msg = models.TextField()
    file = models.FileField(upload_to='images/', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date']
