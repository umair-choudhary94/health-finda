
from django.urls import path
from .views import *
urlpatterns = [
    path("",index,name="home"),
    path("contact/",contact_submit),
    path("about/",about),
    path("profile/",profile,name="profile"),
    path('create_patient_profile/', create_patient_profile, name='create_patient_profile'),
    path('create_doctor_profile/', create_doctor_profile, name='create_doctor_profile'),
    path('appointments/<int:appointment_id>/approve/', approve_appointment, name='approve_appointment'),
    path('search/', search_doctors, name='search_doctors'),
    path("doctor/<str:name>/",getdoctor,name="doctor"),
    path("makeappointment/<int:id>/",makeappointment,name="makeappointment"),
    path("addnotice/<str:name>/",addnotice,name="addnotice"),
    path("addreview/<str:name>/",addreview,name="addreview"),
    path("addavailablity/<str:name>/",addavailablity,name="addavailablity"),
    path("addinsuranceinfo/",addinsuranceinfo,name="addinsuranceinfo"),
    path("addcontactinfo/",addcontactinfo,name="addcontactinfo"),
    path("patient/<int:id>/",getpatient,name="getpatient"),
    path("addnote/",addnote,name="addnote")
    
]