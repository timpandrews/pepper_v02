from django.conf.urls import url

from comments.views import (
    comment_delete
)

urlpatterns = [
    url(r'^comment/(?P<id>\d+)/delete/$', comment_delete, name='delete'),
]