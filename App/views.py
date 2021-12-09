from django.shortcuts import render
import razorpay
import stripe
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
from django.conf import settings

def home(request):
    return render(request,'index.html')
def handle(request):
    return render(request,'handle.html')

def razorpay(request):
    if request.method == "POST":
        name = request.POST.get('name')
        amount = request.POST.get('amount')
        client = razorpay.Client(
            auth=("rzp_test_mi8T0oAeZqQK9N", "tHjBjVaC0To5P7iTcJ15HYX4"))

        payment = client.order.create({'amount': amount, 'currency': 'INR',
                                       'payment_capture': '1'})
    return render(request,'razorpay.html')

def stripe(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    stripe.public_key = settings.STRIPE_PUBLISHABLE_KEY


    return render(request,'stripe.html')
#@csrf_exempt
#def stripe(request):
#    if request.method == "POST":
#        name = request.POST.get('name')
#        amount=500
#        customer = stripe.Customer.create(
#            email='customer@example.com',
#            source=data['stripeToken'],
#        )
#        charge = stripe.Charge.create(
#            customer=customer.id,
#            description='Custom t-shirt',
#            amount=amount,
#            currency='inr',
#        )
#    return render(request, 'index.html')


#def charge(request):
#    if request.method == "POST":
#        charge = stripe.Charge.create(
#            amount=500,
#            currency='inr',
#            description='Payment Gateway',
#            source=request.POST['stripeToken']
#        )

@csrf_exempt
def success(request):
    return render(request, "success.html")