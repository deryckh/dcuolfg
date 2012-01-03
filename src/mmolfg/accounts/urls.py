"""
URLS used for accounts management.
"""

from django.conf.urls.defaults import (
    include,
    patterns,
    url,
)
from registration.forms import RegistrationFormUniqueEmail
from registration.views import register

urlpatterns = patterns('',
    url(r'^register/$',
        register, {'form_class': RegistrationFormUniqueEmail},
        name='registration_register'),
    (r'', include('registration.urls')),
)
