from django.conf.urls import url

from journal.api.views import (
    JournalDetailAPIView_by_id,
    JournalDetailAPIView_by_slug,
    JournalListAPIView,
)

urlpatterns = [
    url(r'^$', JournalListAPIView.as_view(), name='journal'),
    # url(r'^journal/create/$', journal_create, name='create'),
    url(r'^(?P<pk>\d+)/$', JournalDetailAPIView_by_id.as_view(), name='detail'),
    url(r'^slug/(?P<slug>[\w-]+)/$', JournalDetailAPIView_by_slug.as_view(), name='detail_slug'),
    # url(r'^journal/(?P<slug>[\w-]+)/edit/$', journal_update, name='update'),
    # url(r'^journal/(?P<slug>[\w-]+)/delete/$', journal_delete, name='delete'),
]