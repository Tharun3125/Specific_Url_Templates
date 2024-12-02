from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def Auto(request):
    return HttpResponse('<center><h1>Very Good Auto is nearby..</h1></center>')