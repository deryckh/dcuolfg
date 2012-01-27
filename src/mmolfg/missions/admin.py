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
    pass


class MissionAdmin(admin.ModelAdmin):
    """Adming class for Mission."""
    list_filter = (
        'mission_type',
        'num_players',
    )
    list_display = (
        'name',
        'mission_type',
        'short_name',
        'location',
    )

admin.site.register(Location, LocationAdmin)
admin.site.register(Mission, MissionAdmin)
