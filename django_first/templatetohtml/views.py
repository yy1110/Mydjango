from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def indextotemp(request):
    three_index = loader.get_template('indextotemp.html')

    result = three_index.render()

    print(result)

    return HttpResponse(result)