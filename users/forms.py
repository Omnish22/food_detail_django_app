from django import forms
from django.contrib.auth.models import User  # we need models to create form
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    # add another field
    # email = forms.EmailField() # alredy defined field


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']