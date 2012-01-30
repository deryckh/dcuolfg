"""
MMOLFG site-wide views.
"""

from django.shortcuts import render

from mmolfg.missions.models import Mission


def index(request):
    """The site's main index/home page."""
    missions = Mission.objects.featured()
    data = {
        'missions': missions,
        'mission_count': Mission.objects.featured_count(),
    }
    return render(request, 'home.html', data)
