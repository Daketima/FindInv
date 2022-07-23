from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class registerform(UserCreationForm):
    email=forms.EmailField()
    country=forms.Field()
    age=forms.IntegerField()

    class meta:
        model = User
        fields = [
            "Username",
            "Firstname",
            "lastname",
            "age",
            "email",
            "password1"
            "password2"
            "User-type",
            "gender",
        ]
