from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    context = {

    }
    return render(request, "home.html", context)

def journal(request):
    context = {

    }
    return render(request, "journal.html", context)

def page1(request):
    context = {
        "title": "Page 1",
    }
    return render(request, "page1.html", context)
