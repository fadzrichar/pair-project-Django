from django import forms
from .models import *


class UserForm(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = User
        fields = '__all__'