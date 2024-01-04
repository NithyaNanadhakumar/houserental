from django.urls import path
from User import views
app_name="user"

urlpatterns = [
    path('ushom/',views.ushomepage,name="home"),
    path('usmypro/',views.usprofile,name="usmypro"),
    path('editus/<int:eid>',views.editusprofile,name="editusprofile"),
    path('changeuspass/<int:cid>',views.Changeuspass,name="changeuspass"),
    path('searchrent/',views.searchrent,name="searchrent"),
    path('ajaxrent/',views.Ajaxrent,name="Ajax-rent"),
    path('conf/<int:rid>',views.confhomepage,name="conf"),
    path('usfeed/',views.userfeedback,name="usfeed"),
    path('myorders/',views.Myorders,name="MyBooking"),
    path('pay/<int:pid>',views.Payment,name="pay"),
    path('Loader/',views.Loader,name="Loader"),
    path('Sucesser/',views.Sucesser,name="Sucesser"),
    path('uscom/',views.usercomplaint,name="uscom"),
    path('viewgallery/<int:rid>',views.viewgallery,name="gallery"),
    path('logout/',views.logout,name="logout"),

]