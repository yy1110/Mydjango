from django.contrib import admin
from django.urls import path
from App import views

urlpatterns=[
    path('addpersons/', views.add_persons, name = 'addpersons')
]