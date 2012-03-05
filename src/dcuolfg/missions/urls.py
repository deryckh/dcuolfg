"""
URLS used for missions in mmolfg.
"""

from django.conf.urls.defaults import (
    patterns,
    url,
)

from mmolfg.missions.views import (
    location_index,
    mission_index,
)

urlpatterns = patterns('',
    url(
        r'locations/(?P<slug>[-\w]+)/$', location_index,
        name='location_index'),
    url(r'(?P<slug>[-\w]+)/$', mission_index, name='mission_index'),
)
