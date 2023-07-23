from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect

from touch.models import Touch  #(FOR FORM DATA)

def homePage(request):
     return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def certificates(request):
    return render(request,"certificates.html")

def education(request):
    return render(request,"education.html")

def gallery(request):
    return render(request,"gallery.html")

def image(request):
    return render(request,"image.html")

# GET FORM DATA
def saveEnquiry(request):
    
    if request.method=="POST":
        Name=request.POST.get('Name')
        Email=request.POST.get('Email')
        Massage=request.POST.get('Massage')
        data=Touch(name=Name,email=Email,massage=Massage)
        data.save()
    return render(request,"index.html")