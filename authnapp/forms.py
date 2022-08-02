from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from authnapp.models import CustomUser


class DataInput(forms.DateInput):
    input_type = 'date'


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'gender',
            'birth_date'
        )
        widgets = {
            'birth_date': DataInput(),
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'gender',
            'birth_date'
        )
        widgets = {
            'birth_date': DataInput(),
        }