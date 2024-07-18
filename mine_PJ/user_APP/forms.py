from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUp(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}), required=True, label='')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), required=True, label='')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}), required=True,
                                label='')
    class Meta:
        model = User
        fields = 'username', 'password1', 'password2'


class SignIn(forms.Form):
    username = forms.CharField(widget=forms.TextInput(), required=True , label='')
    password = forms.CharField(widget=forms.PasswordInput(), required=True , label='')
