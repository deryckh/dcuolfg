"""
Models for missions in DCUO LFG.
"""

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Mission(models.Model):
    """Mission the base class for grouping together in DCUO LFG."""

    MISSION_TYPE_CHOICES = (
        (0, 'Areana PVP'),
        (1, 'Alert'),
        (2, 'Legends PVP'),
        (3, 'Raid'),
        (4, 'Duo'),
        (5, 'Bounty'),
        (6, 'Character leveling'),
    )

    mission_type = models.IntegerField(
        _('mission type'), choices=MISSION_TYPE_CHOICES, default=1)
