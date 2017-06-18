from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    context = {
        "title": "Pepper v02",
    }
    return render(request, "home.html", context)

def page1(request):
    context = {
        "title": "Pepper v02",
    }
    return render(request, "page1.html", context)
