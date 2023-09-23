from django import forms
from django.contrib.auth.forms import UserCreationForm


class cadastrar(UserCreationForm):
    class Meta:
        
        fields = ('name', 'email','nickname' , 'pass')