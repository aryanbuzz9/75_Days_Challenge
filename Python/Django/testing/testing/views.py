from django.http import HttpResponse
from django.shortcuts import render

def demo(request):
    return HttpResponse("Demo Purpose")

def bootstrap(request):
    return render(request,'index.html')