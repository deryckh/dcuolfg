# Copyright 2012-2013 Deryck Hodge.  This software is licensed under the
# GNU Lesser General Public License version 3 (see the file LICENSE).

"""
URLS used for Characters in dcuolfg.
"""

from django.conf.urls.defaults import (
    patterns,
    url,
)
from django.views.generic.simple import direct_to_template

from dcuolfg.characters import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='characters_index'),
    url(r'^add/$', views.add_character, name='add_character'),
    url(r'^delete/success/$', direct_to_template,
        {'template': 'characters/delete_success.html'},
        name='delete_character_success'),
    url(r'^(?P<server>[-\w]+)/(?P<name>[-\w]+)/$', views.character_profile,
        name='character_profile'),
    url(r'^(?P<server>[-\w]+)/(?P<name>[-\w]+)/delete/$',
        views.delete_character, name='delete_character'),
)
