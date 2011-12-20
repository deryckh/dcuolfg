DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'sqlite3',
        'NAME': '/tmp/mmolfg.db',
    }
}

INSTALLED_APPS = (
    'mmolfg',
)
