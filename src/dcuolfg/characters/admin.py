# Copyright 2012 Deryck Hodge.  This software is licensed under the
# GNU Lesser General Public License version 3 (see the file LICENSE).

"""
Setup admin for character app.
"""

from django.contrib import admin

from sorl.thumbnail.admin import AdminImageMixin

from dcuolfg.characters.models import (
    Character,
    LFGRequest,
)


class CharacterAdmin(AdminImageMixin, admin.ModelAdmin):
    """Admin class for Character."""
    pass

admin.site.register(Character, CharacterAdmin)
admin.site.register(LFGRequest)
