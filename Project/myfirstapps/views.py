from django.shortcuts import render
from django.http import HttpResponse

def user(request):
    return render(request,'index.html')
def sec(request):
    return render(request,'base.html')