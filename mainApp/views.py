from django.shortcuts import render, HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth import login, authenticate
from .models import *
def homePage(Request):
    products=Product.objects.all().order_by("-id")[0:9]
    return render(Request,'index.html',{'products':products,})

def contactPage(Request):
    if(Request.method=="POST"):
        c=Contact()
        c.name=Request.POST.get('name')
        c.lastname=Request.POST.get('lastname')
        c.phone=Request.POST.get('phone')
        c.email=Request.POST.get('email')
        c.message=Request.POST.get('message')
        c.save()
    return render(Request,'contact.html')


def aboutPage(Request):
    gallery=Gallery.objects.all().order_by("-id")
    return render(Request,'about.html',{'gallery':gallery})

def productPage(Request):
    products=Product.objects.all().order_by("id")
    results=Result.objects.all().order_by("id")
    return render(Request,'products.html',{'products':products,'results':results})


def searchPage(Request):
    if(Request.method=="POST"):
        search=Request.POST.get('search')
        products=Product.objects.filter(Q(name__icontains=search))
        return render(Request,'products.html',{'products':products})
    
    else:
        return HttpResponseRedirect("/")
    

def subscribePage(Request):
    if(Request.method=="POST"):
        n=Newsletter()
        email=Request.POST.get("subscribe")
        n.email=email
        n.save()
        return HttpResponseRedirect("/")
    
def loginPage(Request):
    if (Request.method == "POST"):
        username = Request.POST.get("username")
        password = Request.POST.get("password")
        user = authenticate(username=username, password=password)
        if (user is not None):
            login(Request, user)
            if (user.is_superuser):
                return HttpResponseRedirect("/admin/")
            else:
                return HttpResponseRedirect("/")
        else:
            pass
    return render(Request, 'login.html')
    