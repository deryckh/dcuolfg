"""
Models for characters in mmolfg.
"""

from django.db import models


class Character(models.Model):
    """Characters used by Players in DCUO."""

    name = models.CharField(max_length=75)

    # def __unicode__(self):
    #     return u"Character"
