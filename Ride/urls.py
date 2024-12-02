from django.urls import path
from Ride.views import *

urlpatterns =[
    path('Auto/',Auto,name='Auto'),
]