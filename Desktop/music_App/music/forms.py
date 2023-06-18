from django import forms
from .models import MusicFile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class MusicFileForm(forms.ModelForm):
    class Meta:
        model = MusicFile
        fields = ['file', 'title', 'artist', 'genre']

User = get_user_model()
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']