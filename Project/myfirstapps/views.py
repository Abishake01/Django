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
        feed=Feedback(request.POST)
        if feed.is_valid():
            title=request.POST['title']
            subject=request.POST['subject']
            mydir={
                'form':Feedback()
            }
            if title != title.upper():
                mydir['error']=True
                mydir['errormsg']='Title Should be in Capital Letter'
                return render(request,'form.html',context=mydir)
            else:
                mydir['success']=True
                mydir['successmsg']='Form Submitted'
                return render(request,'form.html',context=mydir)
           
    elif request.method =='GET':
        feed= Feedback()
        mydic={
            'form':feed
        }
        return render(request,'form.html',context=mydic)
def photo(request):
    return render(request,'photo.html')