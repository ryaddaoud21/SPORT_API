

from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PersonForm(forms.ModelForm):
    class Meta :
        model = Person
        fields = ['Username','Password']

class ChangeForm(forms.Form):

    id = forms.CharField(label='id', max_length=100)
    old = forms.CharField(label='old', max_length=100)
    new = forms.CharField(label='new', max_length=100)

class Addform(forms.ModelForm):
    class Meta :
        model = Add
        fields = '__all__'

