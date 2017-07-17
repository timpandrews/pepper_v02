from django.contrib import messages
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect

from comments.models import Comment


def comment_delete(request, id):
    comment = get_object_or_404(Comment, id=id)
    journal_URL = comment.content_object.get_absolute_url()

    # if delete confirmed the delete & return to journal detail page
    if request.method == "POST":
        comment.delete()
        messages.success(request, "this has been deleted.")
        return HttpResponseRedirect(journal_URL)

    # else go to delete confirmation page
    context = {
        'object': comment,
        'return_url': journal_URL
    }
    return  render(request, "confirm_delete.html", context)
