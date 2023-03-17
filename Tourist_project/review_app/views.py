from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def mumbai(request):
    m=cdf_mumbai.objects.all() # Collect all records from table

    return render(request,'Mumbai.html',{'m':m})

def agra(request):
    m=cdf_agra.objects.all() # Collect all records from table

    return render(request,'Agra.html',{'m':m})

def pune(request):
    m=cdf_pune.objects.all() # Collect all records from table

    return render(request,'Pune.html',{'m':m})

def goa(request):
    m=cdf_goa.objects.all() # Collect all records from table

    return render(request,'Goa.html',{'m':m})

def ahmedabad(request):
    m=cdf_ahmedabad.objects.all() # Collect all records from table

    return render(request,'Ahmedabad.html',{'m':m})

def udaipur(request):
    m=cdf_udaipur.objects.all() # Collect all records from table

    return render(request,'Udaipur.html',{'m':m})

def jaipur(request):
    m=cdf_jaipur.objects.all() # Collect all records from table

    return render(request,'Jaipur.html',{'m':m})

def chandigarh(request):
    m=cdf_chandigarh.objects.all() # Collect all records from table

    return render(request,'Chandigarh.html',{'m':m})

def New_Delhi(request):
    m=cdf_delhi.objects.all() # Collect all records from table

    return render(request,'New_Delhi.html',{'m':m})

def bangalore(request):
    m=cdf_bangalore.objects.all() # Collect all records from table

    return render(request,'Bangalore.html',{'m':m})

def kolkata(request):
    m=cdf_kolkata.objects.all() # Collect all records from table

    return render(request,'Kolkata.html',{'m':m})

def varanasi(request):
    m=cdf_varanasi.objects.all() # Collect all records from table

    return render(request,'Varanasi.html',{'m':m})

