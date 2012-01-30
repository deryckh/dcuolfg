"""
Base settings.
"""

SITE_ID = 1

DEBUG = True
TEMPLATE_DEBUG = DEBUG

INTERNAL_IPS = ('127.0.0.1',)

DATABASES = {
    'default': {
        'ENGINE': 'sqlite3',
        'NAME': '/tmp/mmolfg.db',
    }
}

# Registration and Accounts
ACCOUNT_ACTIVATION_DAYS = 7
AUTH_PROFILE_MODULE = 'accounts.Profile'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.csrf.CsrfResponseMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'mmolfg.urls'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'registration',
    'sorl.thumbnail',
    'debug_toolbar',
    'mmolfg.accounts',
    'mmolfg.characters',
    'mmolfg.missions',
)
