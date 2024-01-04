from django.db import models
from Admin.models import *


# Create your models here.

class officerreg(models.Model):
    name=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    email=models.EmailField(unique=True,null=True)
    address=models.TextField(null=True)
    gender=models.CharField(max_length=5,null=True)
    zipcode=models.CharField(max_length=50,null=True)
    state=models.ForeignKey(State,on_delete=models.CASCADE)
    photo=models.FileField(upload_to='Officerphoto/')
    proof=models.FileField(upload_to='Officerproof/')
    password=models.CharField(max_length=50,unique=True) 
    doj=models.DateField(auto_now=True)
    vstatus=models.IntegerField(default=0) 