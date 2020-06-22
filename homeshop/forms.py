from django import forms
from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):
    confirm_password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields = ['username','password','confirm_password','first_name','last_name','email']
