from django.shortcuts import render
from .models import MobileTable
from django.views.generic import DetailView
# Create your views here.
def home_view(request):
    return render(request,'homeshop/home.html')
def mobile_view(request):
    mobiles=MobileTable.objects.all()
    return render(request,'homeshop/mobiles.html',{'mobiles':mobiles})
def mobile_detail_view(request,id):
    mobile=MobileTable.objects.get(id=id)
    return render(request,'homeshop/mobile_detail.html',{'mobile':mobile})
def cart_view(request):
    mobiles=MobileTable.objects.all()
    return render(request,"homeshop/cart.html",{'mobiles':mobiles})
