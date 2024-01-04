from django.urls import path
from Owner import views
app_name="owner"

urlpatterns = [
    path('owhom/',views.owhomepage,name="home"),
    path('owmypro/',views.owprofile,name="owmypro"),
    path('editow/<int:eid>',views.editowprofile,name="editowprofile"),
    path('changeowpass/<int:cid>',views.Changeowpass,name="changeowpass"),
    path('rent/',views.rentdetails,name="rent"),
    path('delret/<int:did>',views.delrentdetails,name="delrentdetails"),

    path('viewbookings/',views.Bookking,name="viewbookings"),
    path('acceptbook/<int:aid>',views.Acceptbooking,name="acceptbook"),
    path('rejectbook/<int:rid>',views.Rejectbooking,name="rejectbook"),
    path('acceptedlist/',views.Acclist,name="acclist"),
    path('rejectedlist/',views.Rejlist,name="rejlist"),

    path('owfeed/',views.ownerfeedback,name="owfeed"),
    path('owcom/',views.ownercomplaint,name="owcom"),

    path('galry/<int:rid>',views.Gallery,name="galry"),
    path('logout/',views.logout,name="logout"),

]