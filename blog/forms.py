from django import forms

class UserRegisteration(forms.Form):
    username = forms.CharField(max_length=15)
    email_id = forms.EmailField(max_length=20)