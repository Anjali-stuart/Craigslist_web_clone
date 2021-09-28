from django.shortcuts import render
from django.http import HttpResponse


# from http import request,
# Create your views here.
#  request hadler

# we had to install all the apps in setting register  Installed app
# http is a request response protocol
# takes request and give response


# def hello(request):
#     return HttpResponse('<h1> This is Http GET request</h1>')

def home(request):
    return render(request, "my_app/template/base.html")
