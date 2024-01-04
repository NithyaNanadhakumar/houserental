from django.shortcuts import render,redirect
from Subadmin.models import *
from Admin.models import *
from Guest.models import *
# Create your views here.

def homepage(request):
    sa=subadmin.objects.get(id=request.session['sid'])
    return render(request,"Subadmin/Homepage.html",{'SA':sa})


def profile(request):
    prof=subadmin.objects.get(id=request.session['sid'])
    return render(request,"Subadmin/Myprofile.html",{'PF':prof})



def editprofile(request,eid):
    prof=subadmin.objects.get(id=eid)
    if request.method=="POST":
        prof.name=request.POST.get('txtname')
        prof.contact=request.POST.get('txtcontact')
        prof.email=request.POST.get('txtemail')
        prof.address=request.POST.get('txtaddress')
        prof.save()
        return redirect("subadmin:mypro")
    else:    
        return render(request,"Subadmin/Editmyprofile.html",{'data':prof}) 



def officer(request):
    con=Country.objects.all()
    sta=State.objects.all()
    if request.method=="POST":
        c=Country.objects.get(id=request.POST.get('condrop'))
        sta=State.objects.get(id=request.POST.get('stadrop'))
        officerreg.objects.create(name=request.POST.get('name'),contact=request.POST.get('contact'),email=request.POST.get('email'),address=request.POST.get('address'),gender=request.POST.get('gender'),zipcode=request.POST.get('zip'),state=sta,photo=request.FILES.get('photo'),proof=request.FILES.get('proof'),password=request.POST.get('pw'))
        return render(request,"Subadmin/Officerregistration.html",{'CON':con})
    else:
        return render(request,"Subadmin/Officerregistration.html",{'CON':con})


def Changesubpass(request,cid):
    prof=subadmin.objects.get(id=cid)
    if request.method=="POST":
        psw=prof.password
        old=request.POST.get('Cpass1')
        if old != psw:
            error="Password Not Correct!!"
            return render(request,"Subadmin/Changesubpass.html",{'ERR':error})
        else:
            prof=subadmin.objects.get(id=cid)
            new=request.POST.get('Npass1')
            prof.password=new
            prof.save()
            return redirect('guest:log')
    else:
        return render(request,"Subadmin/Changesubpass.html")        

def userverify(request):
    con=Country.objects.get(id=request.session["cnid"])
    us=userreg.objects.filter(vstatus=1,place__district__state__country=con)
    return render(request,"Subadmin/Userverification.html",{'Us':us})


def acptdetail(request,did):
    us=userreg.objects.get(id=did)
    us.vstatus=3
    us.save()
    return redirect("subadmin:usveri")   



def rejectdetail(request,did):
    us=userreg.objects.get(id=did)
    us.vstatus=4
    us.save()
    return redirect("subadmin:usveri")  

def acceptusr(request):
    con=Country.objects.get(id=request.session["cnid"])
    us=userreg.objects.filter(vstatus=3,place__district__state__country=con)
    return render(request,"Subadmin/Acceptuser.html",{'Us':us})

def urejectdetail(request,did):
    us=userreg.objects.get(id=did)
    us.vstatus=4
    us.save()
    return redirect("subadmin:acept")      


    
def rejectusr(request):
    con=Country.objects.get(id=request.session["cnid"])
    us=userreg.objects.filter(vstatus=4,place__district__state__country=con)
    return render(request,"Subadmin/Rejectuser.html",{'Us':us})

def uacptdetail(request,did):
    us=userreg.objects.get(id=did)
    us.vstatus=4
    us.save()
    return redirect("subadmin:rejct")      


def ownerverify(request):
    con=Country.objects.get(id=request.session["cnid"])
    ow=ownerreg.objects.filter(vstatus=1,place__district__state__country=con)
    return render(request,"Subadmin/Ownerverification.html",{'Ow':ow})  

def owacptdetail(request,did):
    ow=ownerreg.objects.get(id=did)
    ow.vstatus=3
    ow.save()
    return redirect("subadmin:owveri")   
    

def owrejectdetail(request,did):
    ow=ownerreg.objects.get(id=did)
    ow.vstatus=4
    ow.save()
    return redirect("subadmin:owveri") 


def acceptowr(request):
    con=Country.objects.get(id=request.session["cnid"])
    ow=ownerreg.objects.filter(vstatus=3,place__district__state__country=con)
    return render(request,"Subadmin/Acceptowner.html",{'Ow':ow})

def orejectdetail(request,did):
    ow=ownerreg.objects.get(id=did)
    ow.vstatus=4
    ow.save()
    return redirect("subadmin:oacept")   

def rejectowr(request):
    con=Country.objects.get(id=request.session["cnid"])
    ow=ownerreg.objects.filter(vstatus=4,place__district__state__country=con)
    return render(request,"Subadmin/Rejectowner.html",{'Ow':ow})

def oacptdetail(request,did):
    ow=ownerreg.objects.get(id=did)
    ow.vstatus=4
    ow.save()
    return redirect("subadmin:orejct") 


def logout(request):
    del request.session["sid"]
    return redirect("guest:ho")         