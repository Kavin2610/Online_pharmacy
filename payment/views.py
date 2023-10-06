# views.py
import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views import View

stripe.api_key = settings.STRIPE_SECRET_KEY

class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        YOUR_DOMAIN = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_type=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency' : 'usd',
                        'unit_amount': 2000,
                        'product_data': {
                            'name' : 'Stubborn Attachments',
                            #'images' : ['https://i.imgur.com/EHyR2nP.png'],
                        },
                    },
                    'quantity' : 1,
                },

            ],
            mode = 'payment',
            success_url = YOUR_DOMAIN  + '/success/',
            cancel_url = YOUR_DOMAIN  + '/cancel/',
        )

        return JsonResponse({
            'id' : checkout_session.id
        })