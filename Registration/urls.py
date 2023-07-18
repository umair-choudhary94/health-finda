
from django.urls import path
from .views import *
urlpatterns = [
    path("signup/",signup,name="signup"),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('verify/<str:uid>/<str:token>/', verify_email, name='verify_email'),
    
]