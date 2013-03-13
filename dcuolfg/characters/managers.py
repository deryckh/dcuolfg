# Copyright 2012-2013 Deryck Hodge.  This software is licensed under the
# GNU Lesser General Public License version 3 (see the file LICENSE).

"""
Custom managers for characters app.
"""

from django.db import models


# XXX: deryck Requires db-integration test.
# To test this, we have to call save, so it
# needs to be tested in db-integration tests.
class CharacterManager(models.Manager):
    """Provides custom queryset methods for Character objects."""

    def added(self):
        """Get the recently added Character objects."""
        return self.get_query_set().order_by('-date_added')

    def updated(self):
        """Get the recently updated Character objects."""
        return self.get_query_set().order_by('-date_updated')
