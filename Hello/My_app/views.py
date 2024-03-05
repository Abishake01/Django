from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    vusers=[
        {"name":"Prabha","Age":20},
        {"name":"Kp","Age":15},
        {"name":"bala","Age":28},
        {"name":"Abi","Age":30,}
    ]
    return render (request,"index.html",context={"users":vusers})
def users(request):
    return HttpResponse("User Page")