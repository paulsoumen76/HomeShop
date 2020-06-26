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

class LaptopTable(models.Model):
    laptop_name=models.CharField(max_length=50)
    laptop_cost=models.FloatField()
    laptop_desc=models.TextField()
    laptop_img=models.ImageField(upload_to='laptop_image',null=True)

    def __str__(self):
        return self.laptop_name



class SpeakerTable(models.Model):
    speaker_name=models.CharField(max_length=50)
    speaker_cost=models.FloatField()
    speaker_desc=models.TextField()
    speaker_img=models.ImageField(upload_to='speaker_image',null=True)

    def __str__(self):
        return self.speaker_name
class MenJeansTable(models.Model):
    men_jeans_name=models.CharField(max_length=50)
    men_jeans_cost=models.FloatField()
    men_jeans_desc=models.TextField()
    men_jeans_img=models.ImageField(upload_to='menjns_image',null=True)

    def __str__(self):
        return self.men_jeans_name

class MenShirtTable(models.Model):
    men_shirt_name=models.CharField(max_length=50)
    men_shirt_cost=models.FloatField()
    men_shirt_desc=models.TextField()
    men_shirt_img=models.ImageField(upload_to='mensrt_image',null=True)

    def __str__(self):
        return self.men_shirt_name

class MenTshirtTable(models.Model):
    men_tshirt_name=models.CharField(max_length=50)
    men_tshirt_cost=models.FloatField()
    men_tshirt_desc=models.TextField()
    men_tshirt_img=models.ImageField(upload_to='mentrt_image',null=True)

    def __str__(self):
        return self.men_tshirt_name


class WomenKurtaTable(models.Model):
    women_kurta_name=models.CharField(max_length=50)
    women_kurta_cost=models.FloatField()
    women_kurta_desc=models.TextField()
    women_kurta_img=models.ImageField(upload_to='wometa_image',null=True)

    def __str__(self):
        return self.women_kurta_name

class WomenJeansTable(models.Model):
    women_jeans_name=models.CharField(max_length=50)
    women_jeans_cost=models.FloatField()
    women_jeans_desc=models.TextField()
    women_jeans_img=models.ImageField(upload_to='womens_image',null=True)

    def __str__(self):
        return self.women_jeans_name

class WomenTshirtTable(models.Model):
    women_tshirt_name=models.CharField(max_length=50)
    women_tshirt_cost=models.FloatField()
    women_tshirt_desc=models.TextField()
    women_tshirt_img=models.ImageField(upload_to='wo_trt_image',null=True)

    def __str__(self):
        return self.women_tshirt_name
class AllProducts(models.Model):
    women_tshirt=models.ForeignKey(WomenTshirtTable)
    women_kurta=models.ForeignKey(WomenKurtaTable)
    women_jeans=models.ForeignKey(WomenJeansTable)
    men_tshirt=models.ForeignKey(MenTshirtTable)
    men_shirt=models.ForeignKey(MenShirtTable)
    men_jeans=models.ForeignKey(MenJeansTable)
    mobile=models.ForeignKey(MobileTable)
    laptop=models.ForeignKey(LaptopTable)
    speaker=models.ForeignKey(SpeakerTable)

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
