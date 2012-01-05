"""
Devel-only settings.
"""

import os.path

SOURCE_ROOT = os.path.realpath('.')
TEMPLATE_DIRS = (
    '%s/templates' % SOURCE_ROOT,
)
MEDIA_URL = '/media/'
MEDIA_ROOT = '%s/static' % SOURCE_ROOT
