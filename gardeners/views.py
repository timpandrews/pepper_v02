from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render

from gardeners.models import Following

def gardeners_home(request):
    print (request.POST)
    # if 'action' in request.POST:
    #     action = request.GET.get('action')
    # else:
    #     action = 'none'
    action = 'none'
    action = request.GET.get('action')
    print ("action: ", action)
    if request.GET.get('user'):
        user_id = int(request.GET.get('user'))
        print ("user_id: ", user_id)
    if request.GET.get('target'):
        target_id = int(request.GET.get('target'))
        print ("target_id: ", target_id)

    if action == "follow":
        follow = Following(user_id=user_id, following_id=target_id)
        follow.save()
        messages.success(request, "Successfully Added to Following table")
    elif action == "unfollow":
        unFollow = Following.objects.get(user_id=user_id, following_id=target_id)
        unFollow.delete()
        messages.success(request, "Successfully Deleted from Following table")


    gardeners_list = User.objects.exclude(id=request.user.id)
    following_list = Following.objects.filter(user_id=request.user.id).values_list('following_id', flat=True)
    context = {
        "gardeners_list": gardeners_list,
        "following_list": following_list,
        "title": "Gardeners Home",
    }
    return render(request, "gardeners/gardeners.html", context)