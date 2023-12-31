from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.conf import settings
import stripe




def checkout(request):
    stripe.api_key = "sk_test_51Ny5mISFMZ7tthqyGtGIkkrXzTGqFI7KEHVKEtrTLdQAxuNtfJ543UMed9beTC0PcTNYGRjgfDzCtaiQJeYWquhm00FbcfN0rA"

    if request.method == 'POST':
        token = request.POST.get('stripeToken')
        amount = 1000

        try:
            charge = stripe.Charge.create(
                amount = amount,
                currency = 'usd',
                source=token,
                description='example charge',
            )
            return render(request, 'payment/success.html')
        except stripe.error.CardError as e:
            return render(request, 'error.html', {'error':str(e)})
    return render(request, 'payment/checkout.html')    

#flask equivalent
stripe.api_key = 'sk_test_51Ny5mISFMZ7tthqyGtGIkkrXzTGqFI7KEHVKEtrTLdQAxuNtfJ543UMed9beTC0PcTNYGRjgfDzCtaiQJeYWquhm00FbcfN0rA'

# def create_checkout_session(request):
#     YOUR_DOMAIN = 'http://localhost:8000' 
#     price_id = 'price_1OOjl6SFMZ7tthqyiQqHkkHv'

#     try:
#         checkout_session = stripe.checkout.Session.create(
#             line_items=[
#                 {
#                     # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
#                     'price': '{{price_id}}',
#                     'quantity': 1,
#                 },
#             ],
#             mode='payment',
#             success_url=YOUR_DOMAIN + '/success/',
#             cancel_url=YOUR_DOMAIN + '/cancel/',
#         )
#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=500)

#     return HttpResponseRedirect(redirect_to=checkout_session.url)

def success(request):
    return render(request,'payment/success.html')

def cancel(request):
    return render(request,'payment/cancel.html')