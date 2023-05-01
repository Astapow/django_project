from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from django_app.models import Topic


class CreateNewBlog(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    content = forms.CharField(label='Content', max_length=1000)
    topic = forms.ModelMultipleChoiceField(queryset=Topic.objects.all(), widget=forms.CheckboxSelectMultiple)


class Register(forms.Form):
    username = forms.CharField(label='Login', max_length=30)
    password = forms.CharField(label='Password', max_length=16, widget=forms.PasswordInput)
    email = forms.EmailField(label='Email', max_length=30)
    first_name = forms.CharField(label='First name', max_length=20)
    last_name = forms.CharField(label='Last name', max_length=20)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data.get('username'),
            password=self.cleaned_data.get('password'),
            email=self.cleaned_data.get('email'),
            first_name=self.cleaned_data.get('first_name'),
            last_name=self.cleaned_data.get('last_name')
        )
        if commit:
            user.save()
        return user


class CreateNewComment(forms.Form):
    content = forms.CharField(label='Content', max_length=300, widget=forms.Textarea)


class AuthenticationForm(forms.Form):
    username = forms.CharField(max_length=254)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if username and password:
            self.user = authenticate(username=username, password=password)
            if self.user is None:
                raise forms.ValidationError('incorrect name or password')
