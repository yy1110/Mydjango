from django.contrib import admin
from django.urls import path, include
from app2.views import World, Add_user, Get_user, Del_All, Update_user
urlpatterns = [

    path('world/', World, name='app2'),
    path('adduser/', Add_user, name='adduser'),
    path('getuser/', Get_user, name='getuser'),
    path('updateuser/', Update_user, name='updateuser'),
    path('deluser/', Del_All, name='deletuser')
]