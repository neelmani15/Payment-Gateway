from django.urls import path
from .views import home, success, razorpay,stripe,handle

urlpatterns = [
    path('', home, name='home'),
    path('razorpay',razorpay,name='razorpay'),
    path('stripe',stripe,name='stripe'),
    path('handle',handle,name='handle'),
    path('success' , success , name='success')
]