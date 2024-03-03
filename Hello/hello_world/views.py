from django.shortcuts import render,HttpResponse

# Create your views here.

def show(request):
    return HttpResponse('Its Working...')