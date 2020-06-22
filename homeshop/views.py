from django.shortcuts import render, redirect, render_to_response
from .models import MobileTable, OrderTable,OrderUpdate,ContactDetails
from django.views.generic import DetailView
from django.template.loader import get_template
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import datetime
import hashlib
from random import randint
from django.template.context_processors import csrf
from paytm import checksum
Merchant_key = "qxCJW5Ii7YyCawX%"

# Create your views here.
def home_view(request):
    return render(request, 'homeshop/home.html')


def mobile_view(request):
    mobiles = MobileTable.objects.all()
    return render(request, 'homeshop/mobiles.html', {'mobiles': mobiles})


def mobile_detail_view(request, id):
    mobile = MobileTable.objects.get(id=id)
    return render(request, 'homeshop/mobile_detail.html', {'mobile': mobile})


def cart_view(request):
    mobiles = MobileTable.objects.all()
    return render(request, "homeshop/cart.html", {'mobiles': mobiles})


def signup_view(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/accounts/login')
    return render(request, 'homeshop/signup.html', {'form': form})



@login_required
def placeorder_view(request):
    if request.method =='POST':
        amount = request.POST.get('amount')
        print(amount)
        first_name = request.POST["firstname"]
        last_name = request.POST["lastname"]
        email = request.POST["email"]
        mobile = request.POST["phone"]
        user_name = request.POST["username"]
        location = request.POST["location"]
        item_json = request.POST["item_json"]
        state = request.POST["state"]
        country = request.POST["country"]
        zip_code = request.POST["zip"]
        order=OrderTable(amount=amount,
                         first_name=first_name,
                         last_name=last_name,
                         email=email,
                         mobile=mobile,
                         user_name=user_name,
                         location=location,
                         item_json=item_json,
                         zip_code=zip_code,
                         state=state,
                         country=country)
        order.save()
        order_update=OrderUpdate(order_id=order.order_id)
        order_update.save()
        order_id=order.order_id
        success = True
        # return render(request,'homeshop/checkout.html',{'order_id':order_id,'success':success})
        params = {
                "MID": "ClrIro99941539062283",
                "ORDER_ID": str(order_id),
                "CUST_ID": email,
                "TXN_AMOUNT": str(amount),
                "CHANNEL_ID": "WEB",
                "INDUSTRY_TYPE_ID": "Retail",
                "WEBSITE": "WEBSTAGING",
                "CALLBACK_URL":"http://127.0.0.1:8000/paytm/"
            }
        params['CHECKSUMHASH'] = checksum.generate_checksum(params,Merchant_key)
        return render(request,'homeshop/paytm.html',{'params':params})
    return render(request,'homeshop/checkout.html')

@csrf_exempt
def payment_handler(request):
    form = request.POST
    response_dict={}
    for i in form.keys():
        response_dict[i] = form[i]
        if i =='CHECKSUMHASH':
            Checksum = form[i]
    verify=checksum.verify_checksum(response_dict,Merchant_key,Checksum)
    if verify:
        if response_dict['RESPCODE'] =='01':
           print('order success')
           status = True
        else:
           print('order is not success' +response_dict['RESPMSG'])
    return render(request,'homeshop/success.html',{'response_dict':response_dict})
def saved_contact_view(request):
    if request.method =='POST':
        name=request.POST['name']
        print(name)
        email=request.POST['email']
        message=request.POST['message']
        new_contact=ContactDetails(name=name,email=email,message=message)
        new_contact.save()
        # return redirect('/')
    return render(request,'homeshop/contact.html')
