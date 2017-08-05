from django.contrib.auth.models import User
from django.shortcuts import render

def gardeners_home(request):
    gardeners_list = User.objects.exclude(id=request.user.id)
    context = {
        "gardeners_list": gardeners_list,
        "title": "Gardeners Home",
    }
    return render(request, "gardeners/gardeners.html", context)