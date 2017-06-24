from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from journal.forms import JournalForm
from journal.models import Journal

def home(request):
    context = {

    }
    return render(request, "home.html", context)

def journal_create(request):
    form = JournalForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get("title"))
        instance.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "Not Created" )
    context = {
        "form": form,
    }
    return render(request, "journal_form.html", context)

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

def journal_update(request, id=None):
    entry = get_object_or_404(Journal, id=id)
    form = JournalForm(request.POST or None, instance=entry)
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get("title"))
        instance.save()
        messages.success(request, "Successfully Updated" )
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'entry': entry,
        'title': entry.title,
        "form": form,
    }
    return render(request, "journal_form.html", context)

def journal_delete(request, id=None):
    entry = get_object_or_404(Journal, id=id)
    entry.delete()
    messages.success(request, "Successfully Deleted" )
    return redirect('journal:journal')


def page1(request):
    context = {
        "title": "Page 1",
    }
    return render(request, "page1.html", context)
