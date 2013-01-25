# Copyright 2012 Deryck Hodge.  This software is licensed under the
# GNU Lesser General Public License version 3 (see the file LICENSE).

"""
Setup admin for character app.
"""

from django.contrib import admin

from dcuolfg.characters.models import (
    Character,
    LFGRequest,
)


admin.site.register(Character)
admin.site.register(LFGRequest)
