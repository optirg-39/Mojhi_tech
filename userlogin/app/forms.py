from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class SignupForm(UserCreationForm):
    password2 = forms.CharField(label='Conferm Password (again)', widget=forms.PasswordInput) #override
    class Meta:
        model=User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email':'Email'}