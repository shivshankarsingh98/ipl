from django import forms
from django.contrib.auth import authenticate,login,logout

class LoginForm(forms.Form):
    userName=forms.CharField(
        max_length=120,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'UserName'})
    )
    password=forms.CharField(
        max_length=120,
        required=True,
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'})
    )


class SignUpForm(forms.Form):
    username = forms.CharField(
        max_length=120,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UserName'})
    )

    password = forms.CharField(
        max_length=120,
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}
                               )
    )
    first_name = forms.CharField(
        max_length=120,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        max_length=120,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})
    )
    email=forms.CharField(
        max_length=120,
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )