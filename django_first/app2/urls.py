from django.contrib import admin
from django.urls import path, include
from app2.views import World
urlpatterns = [

    path('world/', World, name='app2')

]