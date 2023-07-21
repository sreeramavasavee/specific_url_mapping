from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse('<h1>specific url mapping opperations')

def second(request):
    return HttpResponse('<marquee>this is my second string</marquee>')