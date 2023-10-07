from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'age')
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    age = forms.IntegerField(widget=forms.NumberInput(attrs={
        'placeholder': 'Your age here',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    
    gender = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your gender here',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    bgroup = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your bgroup here',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))


    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists.")
        return email

    
    def clean_username(self):
        username = self.cleaned_data.get('email')
        if len(username) < 1:
            raise forms.ValidationError("The name should be atleast 1 character long")
        return username