from django.conf.urls import url

from journal.views import home, page1

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^page1/$', page1, name='page1'),
]