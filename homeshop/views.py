from django.shortcuts import render, redirect, render_to_response
from .models import *
from django.views.generic import DetailView
from django.template.loader import get_template
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import datetime
import hashlib
import io
from random import randint
from django.template.context_processors import csrf
from paytm import checksum
from random import choice
from xhtml2pdf import pisa
Merchant_key = "qxCJW5Ii7YyCawX%"


# Create your views here.
def home_view(request):
    mobiles=MobileTable.objects.all()[:3]
    laptops=LaptopTable.objects.all()[:3]
    speakers=SpeakerTable.objects.all()[:3]
    menjeans=MenJeansTable.objects.all()[:3]
    menshirts=MenShirtTable.objects.all()[:3]
    mentshirts=MenTshirtTable.objects.all()[:3]
    womenjeans=WomenJeansTable.objects.all()[:3]
    womentshirts=WomenTshirtTable.objects.all()[:3]
    womenkurtas=WomenKurtaTable.objects.all()[:3]
    dict={'mobiles':mobiles,'laptops':laptops,'speakers':speakers,'menjeans':menjeans,'menshirts':menshirts,
    'mentshirts':mentshirts,'womenjeans':womenjeans,'womentshirts':womentshirts,'womenkurtas':womenkurtas}
    return render(request, 'homeshop/home.html',context=dict)
def about_us(request):
    return render(request,'homeshop/about.html')

def mobile_view(request):
    mobiles = MobileTable.objects.all()
    return render(request, 'homeshop/mobiles.html', {'mobiles': mobiles})

def search_view(request):
    q=request.GET.get('search')
    mobiles=MobileTable.objects.filter(mobile_name__icontains=q)
    laptops=LaptopTable.objects.filter(laptop_name__icontains=q)
    speakers=SpeakerTable.objects.filter(speaker_name__icontains=q)
    menjeans=MenJeansTable.objects.filter(men_jeans_name__icontains=q)
    menshirts=MenShirtTable.objects.filter(men_shirt_name__icontains=q)
    mentshirts=MenTshirtTable.objects.filter(men_tshirt_name__icontains=q)
    womenjeans=WomenJeansTable.objects.filter(women_jeans_name__icontains=q)
    womentshirts=WomenTshirtTable.objects.filter(women_tshirt_name__icontains=q)
    womenkurtas=WomenKurtaTable.objects.filter(women_kurta_name__icontains=q)
    if mobiles:
        return render(request, 'homeshop/mobiles.html', {'mobiles': mobiles})
    if laptops:
        return render(request, 'homeshop/laptop.html', {'laptops':laptops})
    if speakers:
        return render(request, 'homeshop/speaker.html', {'speakers':speakers})
    if menjeans:
        return render(request, 'homeshop/menjeans.html', {'menjeans':menjeans})
    if menshirts:
        return render(request, 'homeshop/menshirt.html', {'menshirts':menshirts})
    if mentshirts:
        return render(request, 'homeshop/mentshirt.html', {'mentshirts':mentshirts})
    if womenjeans:
        return render(request, 'homeshop/womenjeans.html', {'womenjeans':womenjeans})
    if womenkurtas:
        return render(request, 'homeshop/womenkurta.html', {'womenkurtas':womenkurtas})
    if womentshirts:
        return render(request, 'homeshop/womentshirt.html', {'womentshirts':womentshirts})

    else:
        return HttpResponse('<h1>Product is not found</h1>')



def laptop_view(request):
    laptops = LaptopTable.objects.all()
    return render(request, 'homeshop/laptop.html', {'laptops':laptops})
def speaker_view(request):
    speakers = SpeakerTable.objects.all()
    return render(request, 'homeshop/speaker.html', {'speakers':speakers})

def menjeans_view(request):
    menjeans = MenJeansTable.objects.all()
    return render(request, 'homeshop/menjeans.html', {'menjeans':menjeans})

def menshirt_view(request):
    menshirts = MenShirtTable.objects.all()
    return render(request, 'homeshop/menshirt.html', {'menshirts':menshirts})

def mentshirt_view(request):
    mentshirts = MenTshirtTable.objects.all()
    return render(request, 'homeshop/mentshirt.html', {'mentshirts':mentshirts})

def womenjeans_view(request):
    womenjeans = WomenJeansTable.objects.all()
    return render(request, 'homeshop/womenjeans.html', {'womenjeans':womenjeans})

def womenkurta_view(request):
    womenkurtas= WomenKurtaTable.objects.all()
    return render(request, 'homeshop/womenkurta.html', {'womenkurtas':womenkurtas})

def womentshirt_view(request):
    womentshirts = WomenTshirtTable.objects.all()
    return render(request, 'homeshop/womentshirt.html', {'womentshirts':womentshirts})

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
    global response_dict
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
def getpdfpage(request):
    context = response_dict
    template = get_template("success.html")
    data = template.render(context)
    response = io.BytesIO()
    pdfpage = pisa.pisaDocument(io.BytesIO(data.encode("UTF-8")),response)
    if not pdfpage.err:
        return HttpResponse(response.getvalue(),content_type = "application/pdf")
    else:
        return HttpResponse("error generated pdf")
