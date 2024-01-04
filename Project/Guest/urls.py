from django.urls import path
from Guest import views
app_name="guest"

urlpatterns = [
    path('log/',views.login,name="log"),
    path('us/',views.user,name="us"),
    path('ajaxplace/',views.Ajaxplace,name="Ajax-place"),
    path('ow/',views.owner,name="ow"),
    path('',views.homee,name="ho"),
    path('vr/',views.ViewRent,name="vr"),
   

   
]