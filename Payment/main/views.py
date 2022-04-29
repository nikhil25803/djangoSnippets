# from gettext import install
from locale import currency
from django.shortcuts import render
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
from rsa import sign

# Create your views here.

# Razorpay authorization
razorpay_client = razorpay.Client(
    auth = (settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET)
)

def index(request):

    currency = 'INR'
    amount = 2000

    # Create a razorpay Id
    razorpay_order = razorpay_client.order.create(dict(
        amount = amount,
        currency = currency,
        payment_capture = '0',
    ))

    # Order Id of newly created order
    razorpay_order_id = razorpay_order['id']
    callback_url = 'paymenthandler/'

    # Pass details to frontend
    context = {
        'razorpay_order_id' : razorpay_order_id,
        'razorpay_merchant_key' : settings.RAZOR_KEY_ID,
        'razorpay_amount' : amount,
        'callback_url' : callback_url,
        'currency' : currency,
    }

    return render(request, 'index.html', context=context)


@csrf_exempt

def paymenthandler(request):

    if request.method == "POST":

        try:
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id' : razorpay_order_id,
                'razorpay_payment_id' : payment_id,
                'razorpay_signature' : signature,
            }

            result = razorpay_client.utility.verify_payment_signature(params_dict)

            if result is None:
                amount = 2000
                
                try:
                    razorpay_client.payment.capture(payment_id, amount)

                    return render(request, 'paymentsuccess.html')
                
                except :

                    return render(request, 'paymentfail.html')

            else:

                return render(request, 'paymentfail.html')

        except :

            return HttpResponseBadRequest()

    else :

        return HttpResponseBadRequest()