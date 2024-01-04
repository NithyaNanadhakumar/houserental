from django.db import models


# Create your models here.
class Renttype(models.Model):
    renttype_name=models.CharField(max_length=50)

    def __str__(self):
        return self.renttype_name


class Country(models.Model):
    country_name=models.CharField(max_length=50)

    def __str__(self):
        return self.country_name


class State(models.Model):
    state_name=models.CharField(max_length=50) 
    country=models.ForeignKey(Country,on_delete=models.SET_NULL,null=True) 

    def __str__(self):
        return self.state_name 


class District(models.Model):
    district_name=models.CharField(max_length=50)
    state=models.ForeignKey(State,on_delete=models.SET_NULL,null=True) 
     

    def __str__(self):
        return self.district_name   


class Place(models.Model):
    place_name=models.CharField(max_length=50)
    district=models.ForeignKey(District,on_delete=models.SET_NULL,null=True) 
 

    def __str__(self):
        return self.place_name    


class subadmin(models.Model):
    name=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    country=models.ForeignKey(Country,on_delete=models.CASCADE)
    photo=models.FileField(upload_to='UserDocs/')
    password=models.CharField(max_length=50)   


class admin(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True,null=True)
    password=models.CharField(max_length=50,unique=True) 


    



 