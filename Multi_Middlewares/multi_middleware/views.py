from django.shortcuts import render,HttpResponse

def Home(request):
    print('This Is Views.py !')
    return HttpResponse("Home Pages !!!")
