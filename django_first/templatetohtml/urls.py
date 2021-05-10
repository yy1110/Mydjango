from django.contrib import admin
from templatetohtml import views
from django.urls import path, include


urlpatterns = [
    path('three_index/', views.indextotemp, name='three_index')
]