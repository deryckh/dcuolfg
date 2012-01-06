"""
Models for user account profiles.
"""

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Profile(models.Model):
    """Main profile model module."""

    user = models.ForeignKey(User)
    real_name = models.CharField(_('real name'), max_length=75,
        blank=True)
