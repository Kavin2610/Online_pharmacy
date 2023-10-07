from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import stripe

def stripe_payment(request):
    if request.method == 'POST':
        
        card_number = request.POST['card_number']
        expiration_month = request.POST['expiration_month']
        expiration_year = request.POST['expiration_year']
        cvc = request.POST['cvc']

        stripe.api_key = settings.STRIPE_SECRET_KEY
        charge = stripe.Charge.create(
            amount=1000,
            currency='usd',
            source=card_number,
            expiration_month=expiration_month,
            expiration_year=expiration_year,
            cvc=cvc
        )
        return HttpResponse('Your payment was successful!')
    else:
      pass