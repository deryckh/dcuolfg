# Copyright 2012 Deryck Hodge.  This software is licensed under the
# GNU Lesser General Public License version 3 (see the file LICENSE).

"""
Setup admin for missions app.
"""

from django.contrib import admin

from sorl.thumbnail.admin import AdminImageMixin

from mmolfg.missions.models import (
    Location,
    Mission,
)


class LocationAdmin(AdminImageMixin, admin.ModelAdmin):
    """Admin class for Location."""
    prepopulated_fields = {'slug': ('name',)}


class MissionAdmin(admin.ModelAdmin):
    """Adming class for Mission."""
    list_filter = (
        'mission_type',
        'num_players',
        'featured',
    )
    list_display = (
        'name',
        'mission_type',
        'featured',
    )
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Location, LocationAdmin)
admin.site.register(Mission, MissionAdmin)
