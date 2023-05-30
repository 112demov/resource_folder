from django.forms import ModelForm
from .models import Room


class CreateChatForm(ModelForm):
    class Meta:
        model = Room
        fields = ['second_user']