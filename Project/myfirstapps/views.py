from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .form import *

def user(request):
    return render(request,'index.html')
def sec(request):
    var='hello world'
    message='List the Animals'
    animal=['monkey','Donkey','Lion','Tiger']
    a,b=5,10
    c=a>b
    
    dict={
        'var':var,
        'msg':message,
        'forest':animal,
        'a':a,
        'b':b,
        'c':c
    }
    return render(request,'base.html',context=dict)
def image(request,imagename):
    myimage=str(imagename);
    myimage=myimage.lower();
    print(myimage)
    if myimage=='django':
        var=True
    elif myimage=='python':
        var=False
    dic={
        'var':var
    }
    return render(request,'image.html',context=dic)
def submitform(request):
    disk={
       'a1':request.Get('Mytext'),
        'a2':request.Get('Mytextarea'),
        'method':request.method
     }
    return JsonResponse(disk)
def form(request):
    if request.method =='POST':
        pass
    elif request.method =='GET':
        feed= Feedback()
        mydic={
            'form':feed
        }
        return render(request,'form.html',context=mydic)