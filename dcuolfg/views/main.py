# Copyright 2012 Deryck Hodge.  This software is licensed under the
# GNU Lesser General Public License version 3 (see the file LICENSE).

"""
Site-wide views.
"""

from django.shortcuts import render

from dcuolfg.missions.models import Mission


def index(request):
    """The site's main index/home page."""
    missions = list(Mission.objects.featured())
    data = {
        'missions': missions,
        'mission_count': len(missions),
    }
    return render(request, 'home.html', data)
