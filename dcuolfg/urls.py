# Copyright 2012 Deryck Hodge.  This software is licensed under the
# GNU Lesser General Public License version 3 (see the file LICENSE).

"""
URLConf for MMOLFG sites.
"""

from django.conf import settings
from django.conf.urls.defaults import (
    include,
    patterns,
    url,
    )

from dcuolfg.views import (\
    dev,
    main,
    )

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^accounts/', include('dcuolfg.accounts.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/$', dev.api, name='api'),
    url(r'missions/', include('dcuolfg.missions.urls')),
    url(r'^$', main.index, name='home'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(
            r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                'document_root': settings.MEDIA_ROOT,
        }),
   )
