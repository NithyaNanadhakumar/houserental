from django.shortcuts import render,redirect
from Subadmin.models import *
from Guest.models import *

# Create your views here.


def ofhomepage(request):
    if 'oid' in request.session:
        return render(request,"Officer/Ofhomepage.html")
    else:
        return redirect("guest:log")
        



def ofprofile(request):
    if 'oid' in request.session:
        off=officerreg.objects.get(id=request.session['oid'])
        return render(request,"Officer/Ofmyprofile.html",{'OF':off})
    else:
        return redirect("guest:log")
        
    



def editofprofile(request,eid):
    if 'oid' in request.session:
        off=officerreg.objects.get(id=eid)
        if request.method=="POST":
            off.name=request.POST.get('txtname1')
            off.contact=request.POST.get('txtcontact1')
            off.email=request.POST.get('txtemail1')
            off.address=request.POST.get('txtaddress1')
            off.zipcode=request.POST.get('txtzip1')
            off.save()
            return redirect("officer:ofmypro")
        else:    
            return render(request,"Officer/Editofmyprofile.html",{'data':off})   
    else:
        return redirect("guest:log")
        


def Changeofpass(request,cid):
    if 'oid' in request.session:
        off=officerreg.objects.get(id=cid)
        if request.method=="POST":
            psw=off.password
            old=request.POST.get('Cpass1')
            if old != psw:
                error="Password Not Correct!!"
                return render(request,"Officer/Changeofpass.html",{'ERR':error})
            else:
                off=officerreg.objects.get(id=cid)
                new=request.POST.get('Npass1')
                off.password=new
                off.save()
                return redirect('guest:log')
        else:
            return render(request,"Officer/Changeofpass.html")
    else:
        return redirect("guest:log")
        
        


def userverify(request):
    if 'oid' in request.session:
        sta=State.objects.get(id=request.session["stid"])
        us=userreg.objects.filter(vstatus=0,place__district__state=sta)
        return render(request,"Officer/Userverification.html",{'Us':us})
    else:
        return redirect("guest:log")
        
        

def acptdetail(request,did):
    if 'oid' in request.session:
        us=userreg.objects.get(id=did)
        us.vstatus=1
        us.save()
        return redirect("officer:usveri") 
    else:
        return redirect("guest:log")
              



def rejectdetail(request,did):
    if 'oid' in request.session:
        us=userreg.objects.get(id=did)
        us.vstatus=2
        us.save()
        return redirect("officer:usveri")
    else:
        return redirect("guest:log")      

def acceptusr(request):
    if 'oid' in request.session:
        sta=State.objects.get(id=request.session["stid"])
        us=userreg.objects.filter(vstatus=1,place__district__state=sta)
        return render(request,"Officer/Acceptuser.html",{'Us':us})
    else:
        return redirect("guest:log")      
    

def urejectdetail(request,did):
    if 'oid' in request.session:
        us=userreg.objects.get(id=did)
        us.vstatus=2
        us.save()
        return redirect("officer:acept")
    else:
        return redirect("guest:log")      
          


    
def rejectusr(request):
    if 'oid' in request.session:
        sta=State.objects.get(id=request.session["stid"])
        us=userreg.objects.filter(vstatus=2,place__district__state=sta)
        return render(request,"Officer/Rejectuser.html",{'Us':us})
    else:
        return redirect("guest:log")      
    

def uacptdetail(request,did):
    if 'oid' in request.session:
        us=userreg.objects.get(id=did)
        us.vstatus=2
        us.save()
        return redirect("officer:rejct")      
    else:
        return redirect("guest:log")      


def ownerverify(request):
    if 'oid' in request.session:
        sta=State.objects.get(id=request.session["stid"])
        ow=ownerreg.objects.filter(vstatus=0,place__district__state=sta)
        return render(request,"Officer/Ownerverification.html",{'Ow':ow})  
    else:
        return redirect("guest:log")      
    

def owacptdetail(request,did):
    if 'oid' in request.session:
        ow=ownerreg.objects.get(id=did)
        ow.vstatus=1
        ow.save()
        return redirect("officer:owveri") 
    else:
        return redirect("guest:log")      
      
    

def owrejectdetail(request,did):
    if 'oid' in request.session:
        ow=ownerreg.objects.get(id=did)
        ow.vstatus=2
        ow.save()
        return redirect("officer:owveri") 
    else:
        return redirect("guest:log")      
    


def acceptowr(request):
    if 'oid' in request.session:
        sta=State.objects.get(id=request.session["stid"])
        ow=ownerreg.objects.filter(vstatus=1,place__district__state=sta)
        return render(request,"Officer/Acceptowner.html",{'Ow':ow})
    else:
        return redirect("guest:log")      
    
def orejectdetail(request,did):
    if 'oid' in request.session:
        ow=ownerreg.objects.get(id=did)
        ow.vstatus=2
        ow.save()
        return redirect("officer:oacept")   
    else:
        return redirect("guest:log")      
    
def rejectowr(request):
    if 'oid' in request.session:
        sta=State.objects.get(id=request.session["stid"])
        ow=ownerreg.objects.filter(vstatus=2,place__district__state=sta)
        return render(request,"Officer/Rejectowner.html",{'Ow':ow})
    else:
        return redirect("guest:log")      
    
def oacptdetail(request,did):
    if 'oid' in request.session:
        ow=ownerreg.objects.get(id=did)
        ow.vstatus=2
        ow.save()
        return redirect("officer:orejct") 
    else:
        return redirect("guest:log")      
           
    


def logout(request):
    del request.session["oid"]
    return redirect("guest:ho")     
    



    