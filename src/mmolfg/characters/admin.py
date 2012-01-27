"""
Setup admin for character app.
"""

from django.contrib import admin

from sorl.thumbnail.admin import AdminImageMixin

from mmolfg.characters.models import (
    Character,
    LFGRequest,
)


class CharacterAdmin(AdminImageMixin, admin.ModelAdmin):
    """Admin class for Character."""
    pass

admin.site.register(Character, CharacterAdmin)
admin.site.register(LFGRequest)
