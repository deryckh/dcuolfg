"""
Base settings.
"""

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
    'mmolfg',
)
