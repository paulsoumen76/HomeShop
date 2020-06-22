from django.db import models
from django.conf import settings
# Create your models here.
class MobileTable(models.Model):
    mobile_name=models.CharField(max_length=20)
    mobile_cost=models.FloatField()
    mobile_desc=models.TextField()
    mobile_img=models.ImageField(upload_to='mobile_image',null=True)

    def __str__(self):
        return self.mobile_name

class OrderTable(models.Model):
    order_id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50,null=True)
    user_name=models.CharField(max_length=5)
    email=models.EmailField(null=True)
    mobile=models.CharField(max_length=40,null=True)
    amount =models.CharField(max_length=30,null=True)
    location=models.CharField(max_length=100,null=True)
    location2=models.CharField(max_length=100,null=True)
    country=models.CharField(max_length=100,null=True)
    state=models.CharField(max_length=100,null=True)
    zip_code=models.CharField(max_length=30,null=True)
    item_json=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.user_name
class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    ordertime = models.DateField(auto_now_add=True)
class ContactDetails(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=30)
    message=models.TextField()
    def __str__(self):
        return self.name
