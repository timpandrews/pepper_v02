from django.conf.urls import url

from gardeners.views import gardeners_home

urlpatterns = [
    url(r'^gardeners/$', gardeners_home, name='gardeners'),
]