

from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PersonForm(forms.ModelForm):
    class Meta :
        model = Person
        fields = ['Username','Password']
