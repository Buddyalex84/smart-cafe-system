from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def Home(request: HttpRequest) -> HttpResponse:
    if request.method=="GET":
        return render(
            request,template_name='home.html', 
        )
    return HttpResponse("This  is home page")
def menu(request: HttpRequest)-> HttpResponse:
    if request.method =="GET":
        return render(
            request,template_name='menu.html',
        )

def About(request: HttpRequest)-> HttpResponse:
    if request.method=="GET":
        return render(
            request,template_name='about.html', 
        )
    return 

def contact(request: HttpRequest)-> HttpResponse:
    if request.method =="GET":
        return render(
            request,template_name='contact.html',
            
        )