from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


clienttype=(
    ("0",""),
    ("1","company"),
    ("2","investor"),
    ("3","idealist"),

)

sex=(
    ("0",""),
    ("1","female"),
    ("2","male"),
)

class registerform(UserCreationForm):
    email=forms.EmailField()
    country=forms.Field()
    age=forms.IntegerField()
    Firstname=forms.TextInput()
    lastername=forms.TextInput()
    user_type=forms.ChoiceField(choices=clienttype)
    gender=forms.ChoiceField(choices=sex)
    class meta:
        model = User
        fields = [
            "Username",
            "Firstname",
            "lastname",
            "age",
            "email",
            "password",
            "User_type",
            "gender",
        ]
