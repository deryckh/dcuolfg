"""
Base settings.
"""

SITE_ID = 1

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'sqlite3',
        'NAME': '/tmp/mmolfg.db',
    }
}

ROOT_URLCONF = 'mmolfg.urls'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'mmolfg',
)
