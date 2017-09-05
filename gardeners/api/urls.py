from django.conf.urls import url

from gardeners.api.views import (
    FollowingDetailAPIView,
    FollowingListAPIView,
)

urlpatterns = [
    url(r'^following/$', FollowingListAPIView.as_view(), name='following'),
    url(r'^following/(?P<id>\d+)/$', FollowingDetailAPIView.as_view(), name='following_detail'),
]