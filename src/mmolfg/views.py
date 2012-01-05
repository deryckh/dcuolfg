"""
MMOLFG site-wide views.
"""

from django.shortcuts import render


def index(request):
    """The site's main index/home page."""
    return render(request, 'home.html', {})
