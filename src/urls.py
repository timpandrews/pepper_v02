"""pepper_v02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

from journal.views import home

from ckeditor_uploader import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^', include("journal.urls", namespace="journal")),
    url(r'^', include("comments.urls", namespace="comments")),
    url(r'^', include("gardeners.urls", namespace="gardeners")),

    url(r'^api/comments/', include("comments.api.urls", namespace="comments-api")),
    url(r'^api/gardeners/', include("gardeners.api.urls", namespace="gardeners-api")),
    url(r'^api/journal/', include("journal.api.urls", namespace="journal-api")),
    url(r'^api/user/', include("profiles.api.urls", namespace="user-api")),

    url(r'^api/auth/token/', obtain_jwt_token),
]

# urlpatterns for ckeditor
urlpatterns += [
        url(r'^upload/', login_required(views.upload), name='ckeditor_upload'),
        url(r'^browse/', never_cache(login_required(views.browse)), name='ckeditor_browse'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
