from django.db import models
from Admin.models import *
from Guest.models import *

# Create your models here.

class Rentdet(models.Model):
    renttype=models.ForeignKey(Renttype,on_delete=models.CASCADE)
    rentname=models.CharField(max_length=50)
    details=models.TextField(null=True)
    image=models.FileField(upload_to='Ownerphoto/')
    amount=models.CharField(max_length=50,null=True)
    owner=models.ForeignKey(ownerreg,on_delete=models.CASCADE)
    vstatus=models.IntegerField(default=0) 


class Ownerfeedback(models.Model):
   owner=models.ForeignKey(ownerreg,on_delete=models.CASCADE)
   content=models.CharField(max_length=5,null=True)    

class gallery(models.Model):
    rent=models.ForeignKey(Rentdet,on_delete=models.CASCADE)
    images=models.FileField(upload_to='galleryDocs/')     
