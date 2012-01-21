"""
Models for characters in mmolfg.
"""

from django.contrib.auth.models import User
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
)
from django.db import models

CHARACTER_SERVER_CHOICES = (
    (0, 'USPS3'),
    (1, 'USPC'),
    (2, 'EUPS3'),
    (3, 'EUPC'),
)


class Character(models.Model):
    """Characters used by Players in DCUO."""

    name = models.CharField(max_length=75)
    server = models.IntegerField(choices=CHARACTER_SERVER_CHOICES)
    player = models.ForeignKey(User, related_name='characters')
    description = models.TextField(blank=True)
    level = models.IntegerField(
        blank=True, null=True, default=1,
        validators=[MinValueValidator(0), MaxValueValidator(30)])
    combat_rating = models.IntegerField(null=True, blank=True, default=0)
    skill_points = models.IntegerField(blank=True, null=True, default=0)

    # XXX: Still need the following attributes:
    #
    # 1.) Role (Controller, Tank, Healer, DPS)
    # 2.) Powerset (Fire, Ice, Mental, Gadgets, Hard light, etc.)
    # 3.) +1 votes

    class Meta:
        """Metadata for Character model."""
        unique_together = ('server', 'name')

    # XXX: Not sure how to model the "looking_for bit yet."
