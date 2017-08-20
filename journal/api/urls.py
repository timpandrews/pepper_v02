from django.conf.urls import url

from journal.api.views import (
    JournalCreateAPIView,

    JournalDeleteAPIView_by_id,
    JournalDeleteAPIView_by_slug,

    JournalDetailAPIView_by_id,
    JournalDetailAPIView_by_slug,

    JournalListAPIView,

    JournalUpdateAPIView_by_id,
    JournalUpdateAPIView_by_slug,
)

urlpatterns = [
    url(r'^$', JournalListAPIView.as_view(), name='journal'),

    url(r'^create/$', JournalCreateAPIView.as_view(), name='create'),

    url(r'^(?P<pk>\d+)/$', JournalDetailAPIView_by_id.as_view(), name='detail'),
    url(r'^slug/(?P<slug>[\w-]+)/$', JournalDetailAPIView_by_slug.as_view(), name='detail_slug'),

    url(r'^(?P<pk>\d+)/delete/$', JournalDeleteAPIView_by_id.as_view(), name='delete'),
    url(r'^slug/(?P<slug>[\w-]+)/delete$/', JournalDeleteAPIView_by_slug.as_view(), name='delete_slug'),

    url(r'^(?P<pk>\d+)/edit/$', JournalUpdateAPIView_by_id.as_view(), name='update'),
    url(r'^slug/(?P<slug>[\w-]+)/edit/$', JournalUpdateAPIView_by_slug.as_view(), name='update_slug'),
]