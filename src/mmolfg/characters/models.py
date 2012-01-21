"""
Models for characters in mmolfg.
"""

from django.contrib.auth.models import User
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
    combat_rating = models.IntegerField(null=True, blank=True)

    ## XXX: Running total of things to add:
    #
    # >> name must be unique per server
    # >> combat rating
    # >> gear
    # >> what is the character looking for?
