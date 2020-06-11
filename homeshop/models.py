from django.db import models

# Create your models here.
class MobileTable(models.Model):
    mobile_name=models.CharField(max_length=20)
    mobile_cost=models.FloatField()
    mobile_desc=models.TextField()
    mobile_img=models.ImageField(upload_to='mobile_image',null=True)

    def __str__(self):
        return self.mobile_name
