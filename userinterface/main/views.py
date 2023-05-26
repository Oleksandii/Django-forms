from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render



def greet(request,name):
    return render(request, 'hello/greet.html',{"name":name })



def index(request):
    return render(request,'hello/index.html')