from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from Subadmin.models import *
from Owner.models import *
# Create your views here.


def login(request):
    if request.method=="POST":
        Email=request.POST.get('email')
        Password=request.POST.get('pw')
        Slogin=subadmin.objects.filter(email=Email,password=Password).count()
        Oflogin=officerreg.objects.filter(email=Email,password=Password).count()
        Uslogin=userreg.objects.filter(email=Email,password=Password).count()
        Owlogin=ownerreg.objects.filter(email=Email,password=Password).count()
        Adlogin=admin.objects.filter(email=Email,password=Password).count()
        if Slogin > 0:
            sadmin=subadmin.objects.get(email=Email,password=Password)
            request.session['sid']=sadmin.id
            request.session["cnid"]=sadmin.country.id
            return redirect('subadmin:home')
        elif Oflogin > 0: 
            offreg=officerreg.objects.get(email=Email,password=Password)
            request.session['oid']=offreg.id
            request.session["stid"]=offreg.state.id
            return redirect('officer:home') 
        elif Uslogin > 0:
            usreg=userreg.objects.get(email=Email,password=Password)
            request.session['uid']=usreg.id
            return redirect('user:home')  
        elif Owlogin > 0:
            owreg=ownerreg.objects.get(email=Email,password=Password)
            request.session['wid']=owreg.id
            return redirect('owner:home')    
        elif Adlogin > 0:
            adreg=admin.objects.get(email=Email,password=Password)
            request.session['aid']=adreg.id
            return redirect('aadmin:home')     
        else:
            error="Invalid Credentials!!"
            return render(request,"Guest/Login.html",{'ERR':error})
    else:
        return render(request,"Guest/Login.html")





def user(request):  
    con=Country.objects.all()
    sta=State.objects.all()
    dis=District.objects.all()
    plc=Place.objects.all()
    if request.method=="POST" and request.FILES:
        c=Country.objects.get(id=request.POST.get('condrop'))
        sta=State.objects.get(id=request.POST.get('stadrop'))
        dst=District.objects.get(id=request.POST.get('distdrop'))
        plc=Place.objects.get(id=request.POST.get('pladrop'))
        userreg.objects.create(name=request.POST.get('uname'),contact=request.POST.get('ucontact'),email=request.POST.get('uemail'),address=request.POST.get('uaddress'),gender=request.POST.get('ugender'),zipcode=request.POST.get('uzip'),place=plc,photo=request.FILES.get('uphoto'),proof=request.FILES.get('uproof'),password=request.POST.get('upw'))
        return render(request,"Guest/Userregistration.html",{'CON':con})
    else:
        return render(request,"Guest/Userregistration.html",{'CON':con})


def Ajaxplace(request):
    dis=District.objects.get(id=request.GET.get('Cntry'))
    plc=Place.objects.filter(district=dis)
    return render(request,"Guest/Ajaxplace.html",{'Plc':plc})  



def owner(request):  
    con=Country.objects.all()
    sta=State.objects.all()
    dis=District.objects.all()
    plc=Place.objects.all()
    if request.method=="POST":
        c=Country.objects.get(id=request.POST.get('condrop'))
        sta=State.objects.get(id=request.POST.get('stadrop'))
        dst=District.objects.get(id=request.POST.get('distdrop'))
        plc=Place.objects.get(id=request.POST.get('pladrop'))
        ownerreg.objects.create(name=request.POST.get('oname'),contact=request.POST.get('ocontact'),email=request.POST.get('oemail'),address=request.POST.get('oaddress'),gender=request.POST.get('ogender'),zipcode=request.POST.get('ozip'),place=plc,photo=request.FILES.get('ophoto'),proof=request.FILES.get('oproof'),password=request.POST.get('opw'))
        return render(request,"Guest/Ownerregistration.html",{'CON':con})
    else:
        return render(request,"Guest/Ownerregistration.html",{'CON':con})      

def homee(request):
    return render(request,"Guest/Home.html")



   
            
def ViewRent(request):
    ren=Rentdet.objects.all()
    return render(request,"Guest/ViewRent.html",{'data':ren})


    