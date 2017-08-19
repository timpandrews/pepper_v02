
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/Users/timandrews/Desktop/apps/pepper_v02/db.sqlite3',
    }
}


STATIC_ROOT = '/Users/timandrews/Desktop/apps/pepper_v02/_static_root'
MEDIA_ROOT = '/Users/timandrews/Desktop/apps/pepper_v02/_media_root'