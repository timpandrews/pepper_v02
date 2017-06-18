from django.conf.urls import url

from journal.views import (
    home,
    journal_create,
    journal_delete,
    journal_detail,
    journal_list,
    journal_update,
    page1
)

urlpatterns = [
    url(r'^journal/$', journal_list, name='journal'),
    url(r'^journal/create/$', journal_create),
    url(r'^journal/delete/$', journal_delete),
    url(r'^journal/detail/$', journal_detail),
    url(r'^journal/update/$', journal_update),
    url(r'^page1/$', page1, name='page1'),
]