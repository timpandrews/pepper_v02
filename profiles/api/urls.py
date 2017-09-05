from django.conf.urls import url
from django.contrib import admin

from profiles.api.views import (
    UserListAPIView,
    UserLoginAPIView
)

urlpatterns = [
    url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
    url(r'^users/$', UserListAPIView.as_view(), name='users'),
]