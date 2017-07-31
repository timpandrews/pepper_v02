from django.shortcuts import render

# Create your views here.

def gardeners_home(request):
    context = {
        "title": "Gardeners Home",
    }
    return render(request, "page1.html", context)