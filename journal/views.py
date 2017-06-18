from django.http import HttpResponse
from django.shortcuts import render

from journal.models import Journal

def home(request):
    context = {

    }
    return render(request, "home.html", context)

def journal_create(request):
    context = {
        'title': 'create'
    }
    return render(request, "journal.html", context)

def journal_detail(request):
    context = {
        'title': 'detail'
    }
    return render(request, "journal.html", context)

def journal_list(request):
    qs = Journal.objects.all()
    context = {
        'journal': qs,
        'title': 'list'
    }
    return render(request, "journal.html", context)

def journal_update(request):
    context = {
        'title': 'upczgd'
    }
    return render(request, "journal.html", context)

def journal_delete(request):
    context = {
        'title': 'delete'
    }
    return render(request, "journal.html", context)

def page1(request):
    context = {
        "title": "Page 1",
    }
    return render(request, "page1.html", context)
