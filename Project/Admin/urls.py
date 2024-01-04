from django.urls import path
from Admin import views
app_name="aadmin"

urlpatterns = [
    path('ret/',views.renttype,name="ret"),
    path('delret/<int:did>',views.delrenttype,name="delrenttype"),
    path('editret/<int:did>',views.editrenttype,name="editrenttype"),

    path('con/',views.country,name="con"),
    path('delcon/<int:did>',views.delcountry,name="delcountry"),
    path('editcon/<int:did>',views.editcountry,name="editcountry"),

    path('sta/',views.state,name="sta"),
    path('delst/<int:did>',views.delstate,name="delstate"),

    path('dist/',views.district,name="dist"),
    path('deldis/<int:did>',views.deldistrict,name="deldistrict"),
    path('ajaxstate/',views.Ajaxstate,name="Ajax-state"),

    path('pla/',views.place,name="pla"),
    path('ajaxdistrict/',views.Ajaxdistrict,name="Ajax-district"),
    path('delplc/<int:did>',views.delplace,name="delplace"),

   path('sub/',views.Subadmin,name="sub"),  

   
    path('adhom/',views.adhomepage,name="home"),  

    path('feed/',views.viewfeedback,name="feed"),
    path('owfeed/',views.Owfeedback,name="owfeed"),

    path('viewcom/',views.COMPLAINT,name="viewcom"),
    path('rply/<int:cid>',views.REPLAY,name="rply"),

    path('logout/',views.logout,name="logout"),

    

]