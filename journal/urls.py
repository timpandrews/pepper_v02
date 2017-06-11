from django.conf.urls import url

from journal.views import home

urlpatterns = [
    url(r'^$', home, name='home'),
]