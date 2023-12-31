from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

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

    age = forms.IntegerField(
        label='Age',
        widget=forms.NumberInput(attrs={'placeholder': 'Your age here', 'class': 'w-full py-4 px-6 rounded-xl'}),
        validators=[MaxValueValidator(100)],
    )

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = forms.ChoiceField(
        label='Gender',
        widget=forms.RadioSelect(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
        choices=GENDER_CHOICES,
    )

    BLOOD_GROUP_CHOICES = [
        ('A+', 'A positive'),
        ('A-', 'A negative'),
        ('B+', 'B positive'),
        ('B-', 'B negative'),
        ('AB+', 'AB positive'),
        ('AB-', 'AB negative'),
        ('O+', 'O positive'),
        ('O-', 'O negative'),
    ]

    bgroup = forms.ChoiceField(
        label='Blood Group',
        widget=forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
        choices=BLOOD_GROUP_CHOICES,
    )


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

    
    # def clean_username(self):
    #     username = self.cleaned_data.get('email')
    #     if len(username) < 1:
    #         raise forms.ValidationError("The name should be atleast 1 character long")
    #     return username
    
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age <= 0 or age < 16:
            raise forms.ValidationError("To use OneYes Pharmacy age should be more than 16")
        if age > 100:
            raise forms.ValidationError("Enter appropriate Age!!!")
        return age
    
    def clean_form(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        age = self.cleaned_data.get('age')
        gender = self.cleaned_data.get('gender')
        bgroup = self.cleaned_data.get('bgroup')
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if (username == "" or email == "" or age == "" or gender == "" or bgroup == "" or password1 == "" or password2 == ""):
            raise forms.ValidationError("Please fill in all the details to proceed further")
        return username, email, age, gender, bgroup, password1, password2
    
   
    
    
    
