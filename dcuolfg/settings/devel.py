# Copyright 2012 Deryck Hodge.  This software is licensed under the
# GNU Lesser General Public License version 3 (see the file LICENSE).

"""
Devel-only settings.
"""

from dcuolfg.settings.common import *
import os.path

DEBUG_TOOLBAR_CONFIG = {
	'INTERCEPT_REDIRECTS': False,
}

SOURCE_ROOT = os.path.realpath('.')
TEMPLATE_DIRS = (
    '%s/templates' % SOURCE_ROOT,
)
MEDIA_URL = '/media'
MEDIA_ROOT = '%s/media' % SOURCE_ROOT
STATIC_URL = '/static'
STATICFILES_DIRS = (
    '%s/static' % SOURCE_ROOT,
)
