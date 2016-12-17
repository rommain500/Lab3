from django import forms
from django.contrib.auth.forms import UserCreationForm

from sauth.models import Client


class RegisterClient(UserCreationForm):

    class Meta:
        model = Client
        fields = (
            'username',
            'language',
        )


class LoginClient(forms.ModelForm):

    class Meta:
        model = Client
        fields = (
            'username',
            'password',
        )
