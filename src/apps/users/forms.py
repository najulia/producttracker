from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CadastroUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "email", "first_name")
