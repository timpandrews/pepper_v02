from django.conf.urls import url

from gardeners.api.views import (
    FollowingListAPIView
)

urlpatterns = [
    url(r'^following/$', FollowingListAPIView.as_view(), name='following'),
    # url(r'^following/(?P<pk>\d+)/$', JournalDetailAPIView_by_id.as_view(), name='following_detail'),
]