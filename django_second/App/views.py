from django.shortcuts import render
from App.models import Person
import random
from django.http import HttpResponse
# Create your views here.
def add_persons(request):
    for i in range(15):
        person = Person()
        flag = random.randrange(100)
        person.p_name = "Tom %s " % i
        person.p_age = flag
        person.p_sex = flag % 2
        person.save()

    return HttpResponse('批量創建成功')
