from django.db import models
from Admin.models import Place


# Create your models here.


class userreg(models.Model):
    name=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    email=models.EmailField(unique=True,null=True)
    address=models.TextField(null=True)
    gender=models.CharField(max_length=5,null=True)
    zipcode=models.CharField(max_length=50,null=True)
    place=models.ForeignKey(Place,on_delete=models.CASCADE)
    photo=models.FileField(upload_to='Userphoto/')
    proof=models.FileField(upload_to='Userproof/')
    password=models.CharField(max_length=50,unique=True) 
    doj=models.DateField(auto_now=True)
    vstatus=models.IntegerField(default=0) 




class ownerreg(models.Model):
    name=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    email=models.EmailField(unique=True,null=True)
    address=models.TextField(null=True)
    gender=models.CharField(max_length=5,null=True)
    zipcode=models.CharField(max_length=50,null=True)
    place=models.ForeignKey(Place,on_delete=models.CASCADE)
    photo=models.FileField(upload_to='Ownerphoto/')
    proof=models.FileField(upload_to='Ownerproof/')
    password=models.CharField(max_length=50,unique=True) 
    doj=models.DateField(auto_now=True)
    vstatus=models.IntegerField(default=0)    

