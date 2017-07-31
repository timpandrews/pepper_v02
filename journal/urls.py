from django.conf.urls import url

from journal.views import (
    journal_create,
    journal_delete,
    journal_detail,
    journal_list,
    journal_update,
)

urlpatterns = [
    url(r'^journal/$', journal_list, name='journal'),
    url(r'^journal/create/$', journal_create, name='create'),
    url(r'^journal/(?P<slug>[\w-]+)/$', journal_detail, name='detail'),
    url(r'^journal/(?P<slug>[\w-]+)/edit/$', journal_update, name='update'),
    url(r'^journal/(?P<slug>[\w-]+)/delete/$', journal_delete, name='delete'),
]