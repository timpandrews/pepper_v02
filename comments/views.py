from django.contrib import messages
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, get_object_or_404

from comments.models import Comment


def comment_delete(request, id):
    try:
        comment = Comment.objects.get(id=id)
    except:
        raise Http404

    journal_URL = comment.content_object.get_absolute_url()

    # check user is owner of comment
    if comment.user != request.user
        response = HttpResponse("You do not have permissions to delete this comment")
        response.status_code = 403
        return response

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
