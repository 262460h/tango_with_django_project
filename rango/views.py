from django.shortcuts import render

from django.http import HttpResponse

def index(request): #questioning if this is the correct way to include a hyperlink
    #must check when I've reconnected to wifi...sometime soon
    return HttpResponse("Rango says hey there partner! <a href='/rango/about/'>About<a/>")

def about(request):
    return HttpResponse("Rango says here is the about page <a href='/rango/'>Index<a/>")