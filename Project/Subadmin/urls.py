from django.urls import path
from Subadmin import views

app_name="subadmin"

urlpatterns = [
    path('hom/',views.homepage,name="home"),
    path('mypro/',views.profile,name="mypro"),
    path('editprof/<int:eid>',views.editprofile,name="editprofile"),
    path('off/',views.officer,name="off"),
    path('changesubpass/<int:cid>',views.Changesubpass,name="changesubpass"),


    path('usveri/',views.userverify,name="usveri"),
    path('acpt/<int:did>',views.acptdetail,name="acptdetail"),
    path('rejt/<int:did>',views.rejectdetail,name="rejectdetail"),
    path('acept/',views.acceptusr,name="acept"),
    path('urejt/<int:did>',views.rejectdetail,name="urejectdetail"),
    path('rejct/',views.rejectusr,name="rejct"),
    path('uracpt/<int:did>',views.uacptdetail,name="uacptdetail"),

    path('owveri/',views.ownerverify,name="owveri"),
    path('owacpt/<int:did>',views.owacptdetail,name="owacptdetail"),
    path('owrejt/<int:did>',views.owrejectdetail,name="owrejectdetail"),
    path('oacept/',views.acceptowr,name="oacept"),
    path('orejt/<int:did>',views.orejectdetail,name="orejectdetail"),
    path('orejct/',views.rejectowr,name="orejct"),
    path('oracpt/<int:did>',views.oacptdetail,name="oacptdetail"),

    path('logout/',views.logout,name="logout"),

]
