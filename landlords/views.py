from django.shortcuts import render
from .models import Landlord

def home(request):
    return render(request,"home.html")

def landlord(request):
    landlords=Landlord.objects.all()
    return render(request,'landlord.html',{'landlords':landlords})

def tenant(request):
    return render (request,"tenant.html")


