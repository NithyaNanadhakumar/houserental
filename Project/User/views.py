from django.shortcuts import render,redirect
from Guest.models import *
from Owner.models import *
from User.models import *

from django.conf import settings
from django.core.mail import send_mail
# Create your views here.


def ushomepage(request):
    return render(request,"User/Ushomepage.html")


def usprofile(request):
    us=userreg.objects.get(id=request.session['uid'])
    return render(request,"User/Usmyprofile.html",{'US':us})    


def editusprofile(request,eid):
    us=userreg.objects.get(id=eid)
    if request.method=="POST":
        us.name=request.POST.get('txtname1')
        us.name=request.POST.get('txtname1')
        us.contact=request.POST.get('txtcontact1')
        us.email=request.POST.get('txtemail1')
        us.address=request.POST.get('txtaddress1')
        us.zipcode=request.POST.get('txtzip1')
        us.save()
        return redirect("user:usmypro")
    else:    
        return render(request,"User/Editusmyprofile.html",{'data':us})     


def Changeuspass(request,cid):
    us=userreg.objects.get(id=cid)
    if request.method=="POST":
        psw=us.password
        old=request.POST.get('Cpass1')
        if old != psw:
            error="Password Not Correct!!"
            return render(request,"User/Changeuspass.html",{'ERR':error})
        else:
            us=userreg.objects.get(id=cid)
            new=request.POST.get('Npass1')
            us.password=new
            us.save()
            return redirect('guest:log')
    else:
        return render(request,"User/Changeuspass.html")    



def searchrent(request):
    con=Country.objects.all()
    ret=Renttype.objects.all()
    rent=Rentdet.objects.all()
    return render(request,"User/SearchRent.html",{'CON':con,'RET':ret,'data':rent})

def Ajaxrent(request):
    if request.GET.get('rid')!="":
        rid=Renttype.objects.get(id=request.GET.get('rid'))
        if request.GET.get('pid')!="":
            pid=Place.objects.get(id=request.GET.get('pid'))
            rent=Rentdet.objects.filter(owner__place=pid,renttype=rid)
            return render(request,"User/AjaxSearch.html",{'data':rent})
        elif request.GET.get('did')!="":
            did=District.objects.get(id=request.GET.get('did'))
            rent=Rentdet.objects.filter(owner__place__district=did,renttype=rid)
            return render(request,"User/AjaxSearch.html",{'data':rent})
        elif request.GET.get('sid')!="":
            sid=State.objects.get(id=request.GET.get('sid'))
            rent=Rentdet.objects.filter(owner__place__district__state==sid,renttype=rid)
            return render(request,"User/AjaxSearch.html",{'data':rent})
        elif request.GET.get('cid')!="":
            cid=Country.objects.get(id=request.GET.get('cid'))
            rent=Rentdet.objects.filter(owner__place__district__state__country=cid,renttype=rid)
            return render(request,"User/AjaxSearch.html",{'data':rent})
        else:
            rent=Rentdet.objects.filter(renttype=rid)
            return render(request,"User/AjaxSearch.html",{'data':rent})
    else:
        if request.GET.get('pid')!="":
            pid=Place.objects.get(id=request.GET.get('pid'))
            rent=Rentdet.objects.filter(owner__place=pid)
            return render(request,"User/AjaxSearch.html",{'data':rent})
        elif request.GET.get('did')!="":
            did=District.objects.get(id=request.GET.get('did'))
            rent=Rentdet.objects.filter(owner__place__district=did)
            return render(request,"User/AjaxSearch.html",{'data':rent})
        elif request.GET.get('sid')!="":
            sid=State.objects.get(id=request.GET.get('sid'))
            rent=Rentdet.objects.filter(owner__place__district__state=sid)
            return render(request,"User/AjaxSearch.html",{'data':rent})
        else:
            cid=Country.objects.get(id=request.GET.get('cid'))
            rent=Rentdet.objects.filter(owner__place__district__state__country=cid)
            return render(request,"User/AjaxSearch.html",{'data':rent})




def confhomepage(request,rid):
    rentd=Rentdet.objects.get(id=rid)
    us=userreg.objects.get(id=request.session['uid'])
    if request.method=="POST":
        Userrequest.objects.create(rent=rentd,user=us)
        return redirect("user:MyBooking")
    else:
        return render(request,"User/Conform.html",{'data':rentd})

   
def userfeedback(request):
    if request.method=="POST":
        us=userreg.objects.get(id=request.session['uid'])
        Userfeedback.objects.create(user=us,content=request.POST.get('txtfeed'))
        return render(request,"User/Userfeedback.html")
    else:
        return render(request,"User/Userfeedback.html")


def Myorders(request):
    userid=userreg.objects.get(id=request.session["uid"])
    bookingdata=Userrequest.objects.filter(user=userid)
    return render(request,"User/MyBooking.html",{'data':bookingdata})

def Payment(request,pid):
    book=Userrequest.objects.get(id=pid)
    user=userreg.objects.get(id=request.session["uid"])
    name=user.name
    email1=user.email
    if request.method=="POST":
        send_mail(
            'Respected Sir/Madam '+ name,#subject
            "Payment Completed SucessFully",#body
            settings.EMAIL_HOST_USER,
            [email1],
        )
        book.vstatus=3
        book.save()
        return redirect("user:Loader")
    else:
        return render(request,"User/Payment.html") 



def Loader(request):
    if 'uid' in request.session:
        return render(request,"User/Loader.html")
    else:
        return redirect("guest:log")

def Sucesser(request):
    if 'uid' in request.session:
        return render(request,"User/Sucesser.html")
    else:
        return redirect("guest:log")




def usercomplaint(request):
    us=userreg.objects.get(id=request.session['uid'])
    cmp=Complaint.objects.filter(user=us)
    if request.method=="POST":
        Complaint.objects.create(user=us,complaint_title=request.POST.get('txt_title'),content=request.POST.get('txtfeed'))
        return render(request,"User/Complaint.html",{'Cmp':cmp})
    else:
        return render(request,"User/Complaint.html",{'Cmp':cmp})




def logout(request):
    del request.session["uid"]
    return redirect("guest:ho")         
     
def viewgallery(request,rid):
    rentd=Rentdet.objects.get(id=rid)
    gal=gallery.objects.filter(rent=rentd)
    return render(request,"User/ViewGallery.html",{'data':gal})