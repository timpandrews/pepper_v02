from django.contrib.auth.models import User
from django.shortcuts import render

from gardeners.models import Following

def gardeners_home(request):
    gardeners_list = User.objects.exclude(id=request.user.id)
    following_list = Following.objects.filter(user_id=request.user.id).values_list('following_id', flat=True)
    context = {
        "gardeners_list": gardeners_list,
        "following_list": following_list,
        "title": "Gardeners Home",
    }
    return render(request, "gardeners/gardeners.html", context)