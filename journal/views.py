from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    context = {
        "title": "Pepper v02",
    }
    return render(request, "home.html", context)
