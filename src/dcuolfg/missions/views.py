# Copyright 2012 Deryck Hodge.  This software is licensed under the
# GNU Lesser General Public License version 3 (see the file LICENSE).

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


def mission_index(request, slug):
    """Returns an index page for a Mission."""
    mission = get_object_or_404(Mission, slug=slug)
    data = {
        'mission': mission,
    }
    return render(request, 'missions/mission_index.html', data)


def location_index(request, slug):
    """Returns an index page for a Location."""
    location = get_object_or_404(Location, slug=slug)
    data = {
        'location': location,
    }
    return render(request, 'missions/location_index.html', data)
