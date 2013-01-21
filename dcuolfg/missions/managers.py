# Copyright 2012 Deryck Hodge.  This software is licensed under the
# GNU Lesser General Public License version 3 (see the file LICENSE).

"""
Custom managers for missions app.
"""

from django.db import models


class MissionManager(models.Manager):
    """Provides custom queryset methods for Mission objects."""

    def featured(self):
        """Returns featured Mission objects."""
        return self.get_query_set().select_related().filter(featured=True)
