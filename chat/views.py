from django.shortcuts import render, redirect
from .models import Message, Room
from django.contrib.auth.decorators import login_required
from .forms import CreateChatForm
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages


def room(request, id):
    room = Room.objects.get(id=id)
    msg = Message.objects.filter(room=room)[0:25]
    return render(request, 'chat/chat.html', {'room': room, 'msg': msg})


def home(request):
    rooms = Room.objects.all()
    return render(request, 'chat/rooms.html', {'rooms':rooms})

def create_room(request):
    users = list(User.objects.all())
    if request.method == 'POST':
        form = CreateChatForm(request.POST)
        if form.is_valid():
            room = Room()
            room.first_user = request.user
            room.second_user = form.cleaned_data['second_user']
            if room.second_user in users:
                room.save()
                return redirect(reverse('room', args=[str(room.id)]))
            else:
                messages.warning(request, 'The recipient is already in the chat list')
    else:
        form = CreateChatForm()

    return render(request, 'chat/add_room.html', {'form': form, 'users':users})

