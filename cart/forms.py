from .models import checkoutdetails
from django import forms
class CheckoutForm(forms.ModelForm):
    class Meta:
        model = checkoutdetails
        fields = ['firstName','lastName', 'address','postalcode', 'city','phoneNumber']

    firstName = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'enter your firstname'}))
    lastName = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'enter your lastname'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'enter your address'}))
    postalcode = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'enter your postalcode'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'enter your city'}))
    phoneNumber = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'enter your phoneNumber'}))
    country = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'enter your country name'}))
    