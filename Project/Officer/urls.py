from django.urls import path
from Officer import views
app_name="officer"

urlpatterns = [
    path('Ofhom/',views.ofhomepage,name="home"),
    path('ofmypro/',views.ofprofile,name="ofmypro"),
    path('editofprof/<int:eid>',views.editofprofile,name="editofprofile"),
    path('changeofpass/<int:cid>',views.Changeofpass,name="changeofpass"),

    path('usveri/',views.userverify,name="usveri"),
    path('acpt/<int:did>',views.acptdetail,name="acptdetail"),
    path('rejt/<int:did>',views.rejectdetail,name="rejectdetail"),
    path('acept/',views.acceptusr,name="acept"),
    path('urejt/<int:did>',views.rejectdetail,name="urejectdetail"),
    path('rejct/',views.rejectusr,name="rejct"),
    path('uracpt/<int:did>',views.acptdetail,name="uacptdetail"),

    path('owveri/',views.ownerverify,name="owveri"),
    path('owacpt/<int:did>',views.owacptdetail,name="owacptdetail"),
    path('owrejt/<int:did>',views.owrejectdetail,name="owrejectdetail"),
    path('oacept/',views.acceptowr,name="oacept"),
    path('orejt/<int:did>',views.orejectdetail,name="orejectdetail"),
    path('orejct/',views.rejectowr,name="orejct"),
    path('oracpt/<int:did>',views.oacptdetail,name="oacptdetail"),


    path('logout/',views.logout,name="logout"),



]
