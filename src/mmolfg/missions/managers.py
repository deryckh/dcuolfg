"""
Custom managers for missions app.
"""

from django.db import models


class MissionManager(models.Manager):
    """Provides custom queryset methods for Mission objects."""

    _featured_cache = None

    def _get_featured(self):
        """Helper method to get the featured mission results."""
        if self._featured_cache is None:
            qs = self.get_query_set()
            self._featured_cache = qs.select_related().filter(featured=True)
        return self._featured_cache

    def featured(self):
        """Returns featured Mission objects."""
        return self._get_featured()

    def featured_count(self):
        """Returns a count of featured missions."""
        featured = self._get_featured()
        return featured.count()
