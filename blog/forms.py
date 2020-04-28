from django import forms
from .models import Post

class UserRegisteration(forms.Form):
    username = forms.CharField(max_length=15)
    email_id = forms.EmailField(max_length=20)


class PostForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)
    # status = forms.BooleanField()

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('posted_date',)