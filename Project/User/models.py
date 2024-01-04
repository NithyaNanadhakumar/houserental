from django.db import models
from Guest.models import *
from Owner.models import *

# Create your models here.

class Userrequest(models.Model):
    user=models.ForeignKey(userreg,on_delete=models.CASCADE)
    rent=models.ForeignKey(Rentdet,on_delete=models.CASCADE)
    vstatus=models.IntegerField(default=0)
    requestdate=models.DateField(auto_now=True)

class Userfeedback(models.Model):
    user=models.ForeignKey(userreg,on_delete=models.CASCADE)
    content=models.CharField(max_length=5,null=True)   


class Complaint(models.Model):
    complaint_title=models.CharField(max_length=400)
    content=models.TextField(null=True)
    date=models.DateField(auto_now=True)
    user=models.ForeignKey(userreg,on_delete=models.SET_NULL,null=True)
    owner=models.ForeignKey(ownerreg,on_delete=models.SET_NULL,null=True)
    complaint_status=models.IntegerField(default=0)
    complaint_replay=models.TextField(null=True,default="not viewed yet")    

