from django.conf.urls import url

from journal.views import (
    journal_create,
    journal_delete,
    journal_detail,
    journal_list,
    journal_update,
    page1
)

urlpatterns = [
    url(r'^journal/$', journal_list, name='journal'),
    url(r'^journal/(?P<id>\d+)/$', journal_detail, name='detail'),
    url(r'^journal/create/$', journal_create, name='create'),
    url(r'^journal/delete/$', journal_delete),
    url(r'^journal/(?P<id>\d+)/edit/$', journal_update, name='update'),
    url(r'^page1/$', page1, name='page1'),
]