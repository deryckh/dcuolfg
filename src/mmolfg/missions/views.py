"""
Views for Mission and Location in mmolfg.
"""

from django.shortcuts import (
    get_object_or_404,
    render,
)

from mmolfg.missions.models import (
    Mission,
    Location,
)


def mission_index(request, name):
    """Returns an index page for a Mission."""
    mission = get_object_or_404(Mission, short_name=name)
    data = {
        'mission': mission,
    }
    return render(request, 'missions/mission_index.html', data)


def location_index(request, name):
    """Returns an index page for a Location."""
    location = get_object_or_404(Location, name=name)
    data = {
        'location': location,
    }
    return render(request, 'missions/location_index.html', data)
