from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    context = {

    }
    return render(request, "home.html", context)

def journal_home(request):
    context = {

    }
    return render(request, "journal.html", context)

def journal_create(request):
    return HttpResponse("<h1>Create</h1>")

def journal_detail(request):
    return HttpResponse("<h1>Detail</h1>")

def journal_list(request):
    return HttpResponse("<h1>List</h1>")

def journal_update(request):
    return HttpResponse("<h1>Update</h1>")

def journal_delete(request):
    return HttpResponse("<h1>Delete</h1>")

def page1(request):
    context = {
        "title": "Page 1",
    }
    return render(request, "page1.html", context)
