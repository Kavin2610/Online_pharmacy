from django import forms

class StripePaymentForm(forms.Form):
        stripe_token = forms.CharField(max_length=255, widget=forms.HiddenInput)
