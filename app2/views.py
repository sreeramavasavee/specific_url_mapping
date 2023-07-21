from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse('<h1><marquee>this is my second app function</marquee></h1>')

def second(request):
    return HttpResponse('<h1><marquee> KRISHNA</marquee></h2>')