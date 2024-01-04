from django.shortcuts import render,redirect
from Admin.models import *
from User.models import *
from Guest.models import*
# Create your views here.

def renttype(request):
    if 'aid' in request.session:
        ret=Renttype.objects.all()
        if request.method=="POST":
            Renttype.objects.create(renttype_name=request.POST.get('r1'))
            return render(request,"Admin/Renttype.html",{'data':ret})
        else:
            return render(request,"Admin/Renttype.html",{'data':ret})
    else:
        return redirect("guest:log")
    

def delrenttype(request,did):
    if 'aid' in request.session:
        ret=Renttype.objects.get(id=did)
        ret.delete()
        return redirect("aadmin:ret")
    else:
        return redirect("guest:log")

 
def editrenttype(request,did):
    if 'aid' in request.session:
        ret=Renttype.objects.get(id=did)
        if request.method=="POST":
            ret.renttype_name=request.POST.get('r1')
            ret.save()
            return redirect("aadmin:ret")
        else:
            return render(request,"Admin/Editrenttype.html",{'data':ret})
    else:
        return redirect("guest:log")        



def country(request):
    con=Country.objects.all()
    if request.method=="POST":
        Country.objects.create(country_name=request.POST.get('c1'))
        return render(request,"Admin/Country.html",{'data':con})
    else:    
        return render(request,"Admin/Country.html",{'data':con})
    

def delcountry(request,did):
    con=Country.objects.get(id=did)
    con.delete()
    return redirect("aadmin:con")


def editcountry(request,did):
    con=Country.objects.get(id=did)
    if request.method=="POST":
        con.country_name=request.POST.get('c1')
        con.save()
        return redirect("aadmin:con")
    else:
        return render(request,"Admin/Editcountry.html",{'data':con})    


def state(request):
    con=Country.objects.all()
    st=State.objects.all()
    if request.method=="POST":
        c=Country.objects.get(id=request.POST.get('condrop'))
        State.objects.create(state_name=request.POST.get('s1'),country=c)
        return render(request,"Admin/State.html",{'con':con,'st':st}) 
    else:
        return render(request,"Admin/State.html",{'con':con,'st':st}) 



def delstate(request,did):
    st=State.objects.get(id=did)
    st.delete()
    return redirect("aadmin:sta") 


def district(request):
    con=Country.objects.all()
    st=State.objects.all()
    dis=District.objects.all()
    if request.method=="POST":
        c=Country.objects.get(id=request.POST.get('condrop'))
        sta=State.objects.get(id=request.POST.get('stadrop'))
        District.objects.create(district_name=request.POST.get('d1'),state=sta)
        return render(request,"Admin/District.html",{'CON':con,'st':st,'Dis':dis})
    else:
        return render(request,"Admin/District.html",{'CON':con,'st':st,'Dis':dis}) 
 


def Ajaxstate(request):
    con=Country.objects.get(id=request.GET.get('Cntry'))
    sta=State.objects.filter(country=con)
    return render(request,"Admin/Ajaxstate.html",{'sta':sta})  


def deldistrict(request,did):
    dis=District.objects.get(id=did)
    dis.delete()
    return redirect("aadmin:dist")        


def place(request):
    con=Country.objects.all()
    st=State.objects.all()
    dis=District.objects.all()
    plc=Place.objects.all()
    if request.method=="POST":
        c=Country.objects.get(id=request.POST.get('Condrop'))
        sta=State.objects.get(id=request.POST.get('stadrop'))
        dst=District.objects.get(id=request.POST.get('distdrop'))
        Place.objects.create(place_name=request.POST.get('p1'),district=dst)
        return render(request,"Admin/Place.html",{'CON':con,'st':st,'Dis':dis,'Plc':plc})
    else:
        return render(request,"Admin/Place.html",{'CON':con,'st':st,'Dis':dis,'Plc':plc}) 



def Ajaxdistrict(request):
    sta=State.objects.get(id=request.GET.get('Cntry'))
    dis=District.objects.filter(state=sta)
    return render(request,"Admin/Ajaxdistrict.html",{'Dis':dis}) 


def delplace(request,did):
    plc=Place.objects.get(id=did)
    plc.delete()
    return redirect("aadmin:pla")


def Subadmin(request):
    if 'aid' in request.session:
        con=Country.objects.all()
        if request.method=="POST" and request.FILES:
            cntry=Country.objects.get(id=request.POST.get('condrop'))
            subadmin.objects.create(name=request.POST.get('name'),contact=request.POST.get('contact'),email=request.POST.get('email'),address=request.POST.get('address'),photo=request.FILES.get('photo'),password=request.POST.get('pw'),country=cntry)
            return render(request,"Admin/Subadmin.html",{'Con':con})
        else:
            return render(request,"Admin/Subadmin.html",{'Con':con})
    else:
        return redirect("guest:log")        
        




def adhomepage(request):
    if 'aid' in request.session:
        return render(request,"Admin/Adminhomepage.html")  
    else:
        return redirect("guest:log")        
                

    
def viewfeedback(request):
    if 'aid' in request.session:
        vw=Userfeedback.objects.all()
        return render(request,"Admin/Viewfeedback.html",{'Vw':vw}) 
    else:
        return redirect("guest:log")        
                
     

        
def Owfeedback(request):
    if 'aid' in request.session:
        of=Ownerfeedback.objects.all()
        return render(request,"Admin/Owviewfeed.html",{'Of':of})  
    else:
        return redirect("guest:log")        
                    


def COMPLAINT(request):
    if 'aid' in request.session:
        ab=Complaint.objects.filter(user__gt=0,complaint_status=0)
        own=Complaint.objects.filter(owner__gt=0,complaint_status=0)
        return render(request,"Admin/ViewComplaint.html",{'Ab':ab,'Own':own})
    else:
        return redirect("guest:log")        
                        

    
def REPLAY(request,cid):
    if 'aid' in request.session:
        br=Complaint.objects.get(id=cid)
        if request.method=="POST":
            br.complaint_replay=request.POST.get('replay')
            br.complaint_status=1
            br.save()
            return redirect("aadmin:viewcom")
        else:
            return render(request,"Admin/Sendreply.html")
    else:
        return redirect("guest:log")        
                        
       

def logout(request):
    del request.session["aid"]
    return redirect("guest:ho")             
