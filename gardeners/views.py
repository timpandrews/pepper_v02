from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render

from gardeners.models import Following

def gardeners_home(request):
    # Get QueryString Parameters if present
    action = 'none'
    action = request.GET.get('action')
    if request.GET.get('user'):
        user_id = int(request.GET.get('user'))
    if request.GET.get('target'):
        target_id = int(request.GET.get('target'))

    # Follows / Unfollow Code
    if action == "follow":
        follow = Following(user_id=user_id, following_id=target_id)
        follow.save()
        messages.success(request, "Successfully Added to Following table")
    elif action == "unfollow":
        unFollow = Following.objects.get(user_id=user_id, following_id=target_id)
        unFollow.delete()
        messages.success(request, "Successfully Deleted from Following table")

    # Build context for gardeners template
    gardeners_list = User.objects.exclude(id=request.user.id)
    following_list = Following.objects.filter(user_id=request.user.id).values_list('following_id', flat=True)
    context = {
        "gardeners_list": gardeners_list,
        "following_list": following_list,
        "title": "Gardeners Home",
    }
    return render(request, "gardeners/gardeners.html", context)