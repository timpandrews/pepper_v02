from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from comments.forms import CommentForm
from comments.models import Comment
from journal.forms import JournalForm
from journal.models import Journal


def home(request):
    context = {

    }
    return render(request, "home.html", context)

def journal_create(request):
    if not request.user.is_authenticated:
        raise Http404
    form = JournalForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "Not Created" )
    context = {
        "form": form,
    }
    return render(request, "journal_form.html", context)

def journal_detail(request, slug=None):
    entry = get_object_or_404(Journal, slug=slug)
    today = timezone.now().date
    comments = Comment.objects.filter_by_instance(entry).order_by('-createTS')

    # Initial values for hidden fields in comment form
    initial_data = {
        "content_type": entry.get_content_type,
        "object_id": entry.id
 	}

    comment_form = CommentForm(request.POST or None, initial=initial_data)

    if comment_form.is_valid():
        c_type = comment_form.cleaned_data.get("content_type")
        content_type = ContentType.objects.get(model=c_type)
        obj_id = comment_form.cleaned_data.get('object_id')
        content_data = comment_form.cleaned_data.get("content")
        new_comment, created = Comment.objects.get_or_create(
            user=request.user,
            content_type=content_type,
            object_id=obj_id,
            content=content_data
        )
        return HttpResponseRedirect(entry.get_absolute_url())

    context = {
        'entry': entry,
        'title': entry.title,
        'today': today,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, "journal_detail.html", context)

def journal_list(request):
    if request.user.is_superuser:
        qs_list = Journal.objects.all().order_by('-createTS')
    else:
        # active() = Custom model manager in models.py
        qs_list = Journal.objects.active().order_by('-createTS')

    query = request.GET.get("q")
    if query:
        qs_list = qs_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)
        ).distinct()

    paginator = Paginator(qs_list, 3)
    page = request.GET.get('page')
    try:
        qs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        qs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        qs = paginator.page(paginator.num_pages)

    today = timezone.now().date

    context = {
        'journal': qs,
        'title': 'list',
        'today': today,
    }
    return render(request, "journal.html", context)

def journal_update(request, slug=None):
    if not request.user.is_authenticated:
        raise Http404
    entry = get_object_or_404(Journal, slug=slug)
    form = JournalForm(request.POST or None, request.FILES or None, instance=entry)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, "Successfully Updated" )
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'entry': entry,
        'title': entry.title,
        "form": form,
    }
    return render(request, "journal_form.html", context)

def journal_delete(request, slug=None):
    if not request.user.is_authenticated:
        raise Http404
    entry = get_object_or_404(Journal, slug=slug)
    entry.delete()
    messages.success(request, "Successfully Deleted" )
    return redirect('journal:journal')

def page1(request):
    context = {
        "title": "Page 1",
    }
    return render(request, "page1.html", context)
