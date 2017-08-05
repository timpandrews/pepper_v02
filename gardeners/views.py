from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.

def gardeners_home(request):
    gardeners_list = User.objects.all()
    context = {
        "gardeners_list": gardeners_list,
        "title": "Gardeners Home",
    }
    return render(request, "gardeners.html", context)