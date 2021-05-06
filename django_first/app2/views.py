from django.shortcuts import render
from django.http import HttpResponse
from hello.models import User
import random
# Create your views here.
count = 0
def World(request):
    return HttpResponse('this is app2')

def Add_user(request):
    global count
    count += 1
    user = User()
    user.user_age = count
    user.user_name = random.choice(['Wang', 'Chan', 'Liu', 'Lin'])
    user.save()
    
    return render(request, ('add_user.html'))

def Get_user(request):

    user1 = User.objects.all()
    context = {
        "user1":user1
    }
    print(context)
    return render(request, ('user_list.html'), context=context)
def Update_user(request):
    pkv = User.objects.values_list()
    randompk = pkv[random.randint(0,len(pkv) -1)][0]
    user = User.objects.get(pk = randompk)
    user.user_name = 'Change'
    user.save()
    response = 'date has been updated'
    return HttpResponse(response)
def Del_All(request):
    pkv = len(User.objects.values_list())
    print(pkv)
    if(pkv > 1):
        pkv = User.objects.values_list()
        randompk = pkv[random.randint(0,len(pkv) -1)][0]
        user = User.objects.get(pk = randompk)
        user.delete()
        response = 'PK ' + str(randompk) + ' has been delete'
        return HttpResponse(response)
    elif(pkv == 1) :
        a = User.objects.values_list()[0][0]
        user = User.objects.get(pk = a)
        user.delete()
        response = 'the ' +str(a)+ ' date has been delete'
        return HttpResponse(response)
    else:
        return HttpResponse('no information')