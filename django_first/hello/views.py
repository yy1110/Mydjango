from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Hello(request):
    return render(request, 'hello.html')



def Testhtml(request):
    return render(request, 'index.html')