"""
Custom managers for missions app.
"""

from django.db import models


class MissionManager(models.Manager):
    """Provides custom queryset methods for Mission objects."""

    def featured(self):
        """Returns featured Mission objects."""
        return self.get_query_set().filter(featured=True)
