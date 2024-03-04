from django.shortcuts import render,HttpResponse

# Create your views here.

def show(request):
    return HttpResponse('Its Working...')
def home(request):
    return HttpResponse('<h1>Home </h1>')