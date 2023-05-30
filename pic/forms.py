from django import forms
from .models import Picture


class CheckImage(forms.ModelForm):

    class Meta:
        model = Pictire
        fields = ['img', 'title',]