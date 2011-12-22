"""
MMOLFG site-wide views.
"""

from django.shortcuts import render


def index(request):
    """The site's main index page."""
    return render(request, 'home.html', {})
