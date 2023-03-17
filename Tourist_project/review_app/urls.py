#app
from django.contrib import admin
from django.urls import path
from review_app import views

urlpatterns = [
    path('',views.index,name='reviews_app'),
    path('mumbai',views.mumbai,name='mumbai'),
    path('goa',views.goa,name='goa'),
    path('ahmedabad',views.ahmedabad,name='ahmedabad'),
    path('pune',views.pune,name='pune'),
    path('jaipur',views.jaipur,name='jaipur'),
    path('bangalore',views.bangalore,name='bangalore'),
    path('kolkata',views.kolkata,name='kolkata'),
    path('varanasi',views.varanasi,name='varanasi'),
    path('new_delhi',views.New_Delhi,name='new_delhi'),
    path('udaipur',views.udaipur,name='udaipur'),
    path('agra',views.agra,name='agra'),
    path('chandigarh',views.chandigarh,name='chandigarh'),
    
]
