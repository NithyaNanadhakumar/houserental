from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from Owner.models import *
from User.models import *
# Create your views here.
from django.conf import settings
from django.core.mail import send_mail

def owhomepage(request):
    if 'wid' in request.session:
        return render(request,"Owner/Owhomepage.html")
    else:
        return redirect("guest:log")      
           
    

    


def owprofile(request):
    if 'wid' in request.session:
        ow=ownerreg.objects.get(id=request.session['wid'])
        return render(request,"Owner/Owmyprofile.html",{'OW':ow})
    else:
        return redirect("guest:log")      
           
        


def editowprofile(request,eid):
    if 'wid' in request.session:
        ow=ownerreg.objects.get(id=eid)
        if request.method=="POST":
            ow.name=request.POST.get('txtname1')
            ow.name=request.POST.get('txtname1')
            ow.contact=request.POST.get('txtcontact1')
            ow.email=request.POST.get('txtemail1')
            ow.address=request.POST.get('txtaddress1')
            ow.zipcode=request.POST.get('txtzip1')
            ow.save()
            return redirect("owner:owmypro")
        else:    
            return render(request,"Owner/Editowmyprofile.html",{'data':ow})  
    else:
        return redirect("guest:log")      
           
                 


def Changeowpass(request,cid):
    if 'wid' in request.session:
        ow=ownerreg.objects.get(id=cid)
        if request.method=="POST":
            psw=ow.password
            old=request.POST.get('Cpass1')
            if old != psw:
                error="Password Not Correct!!"
                return render(request,"Owner/Changeowpass.html",{'ERR':error})
            else:
                ow=ownerreg.objects.get(id=cid)
                new=request.POST.get('Npass1')
                ow.password=new
                ow.save()
                return redirect('guest:log')
        else:
            return render(request,"Owner/Changeowpass.html")  
    else:
        return redirect("guest:log")      
                    



def rentdetails(request):
    if 'wid' in request.session:
        ret=Renttype.objects.all()
        ret1= Rentdet.objects.all()
        ownr=ownerreg.objects.get(id=request.session['wid'])
        if request.method=="POST" and request.FILES:
            r=Renttype.objects.get(id=request.POST.get('retdrop'))
            Rentdet.objects.create(rentname=request.POST.get('rname'),details=request.POST.get('rdetails'),image=request.FILES.get('rimage'),amount=request.POST.get('ramount'),renttype=r,owner=ownr)
            return render(request,"Owner/Rentdetails.html",{'Data':ret,'Ret1':ret1})
        else:
            return render(request,"Owner/Rentdetails.html",{'Data':ret,'Ret1':ret1})
    else:
        return redirect("guest:log")      
                    



def delrentdetails(request,did):
    if 'wid' in request.session:
        ret1=Rentdet.objects.get(id=did)
        ret1.delete()
        return redirect("owner:rent")
    else:
        return redirect("guest:log")      
                    
    

def Bookking(request):
    if 'wid' in request.session:
        ow=ownerreg.objects.get(id=request.session["wid"])
        pdt=Userrequest.objects.filter(rent__owner=ow,vstatus=0)
        return render(request,"Owner/Viewbooking.html",{'Pdt':pdt})
    else:
        return redirect("guest:log")         


def Acceptbooking(request,aid):
    bid=Userrequest.objects.get(id=aid)
    bid.vstatus=1
    bid.save()
    name=bid.user.name
    email1=bid.user.email
    send_mail(
            'Respected Sir/Madam '+ name,#subject
            "Accepted SucessFully",#body
            settings.EMAIL_HOST_USER,
            [email1],
        )
    return redirect("owner:viewbookings")

def Rejectbooking(request,rid):
    bid=Userrequest.objects.get(id=rid)
    name=bid.user.name
    email1=bid.user.email
    bid.vstatus=2
    bid.save()
    send_mail(
            'Respected Sir/Madam '+ name,#subject
            "Rejected SucessFully",#body
            settings.EMAIL_HOST_USER,
            [email1],
        )
    return redirect("owner:viewbookings") 


def Acclist(request):
    ow=ownerreg.objects.get(id=request.session["wid"])
    pdt=Userrequest.objects.filter(rent__owner=ow,vstatus=1)
    return render(request,"Owner/Acceptbooking.html",{'Pdt':pdt})

def Rejlist(request):
    ow=ownerreg.objects.get(id=request.session["wid"])
    pdt=Userrequest.objects.filter(rent__owner=ow,vstatus=2)
    return render(request,"Owner/Rejectbooking.html",{'Pdt':pdt})


def ownerfeedback(request):
    if 'wid' in request.session:
        if request.method=="POST":
            ow=ownerreg.objects.get(id=request.session['wid'])
            Ownerfeedback.objects.create(owner=ow,content=request.POST.get('txtfeed'))
            return render(request,"Owner/Ownerfeedback.html")
        else:
            return render(request,"Owner/Ownerfeedback.html")
    else:
        return redirect("guest:log")         
        



def ownercomplaint(request):
    if 'wid' in request.session:
        ow=ownerreg.objects.get(id=request.session['wid'])
        ocmp=Complaint.objects.filter(owner=ow)
        if request.method=="POST":
            Complaint.objects.create(owner=ow,complaint_title=request.POST.get('txt_title'),content=request.POST.get('txtfeed'))
            return render(request,"Owner/Ocomplaint.html",{'Ocmp':ocmp})
        else:
            return render(request,"Owner/Ocomplaint.html",{'Ocmp':ocmp})
    else:
        return redirect("guest:log")         
        

 



def Gallery(request,rid):
    rentid=Rentdet.objects.get(id=rid)
    if request.method=="POST":
        gallery.objects.create(rent=rentid,images=request.FILES.get('g1'))
        return redirect("owner:rent")
    else:
        return render(request,"Owner/Gallery.html")




def logout(request):
    del request.session["wid"]
    return redirect("guest:ho")     
