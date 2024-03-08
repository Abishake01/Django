from django.shortcuts import render
from django.http import HttpResponse

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
def image(request):
    return render(request,'image.html')