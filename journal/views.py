from django.shortcuts import render, get_object_or_404

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

def journal_detail(request, id=None):
    entry = get_object_or_404(Journal, id=id)
    context = {
        'entry': entry,
        'title': entry.title
    }
    return render(request, "journal_detail.html", context)

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
