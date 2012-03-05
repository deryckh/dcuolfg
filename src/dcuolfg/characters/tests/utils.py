"""
Helper functions for Character tests.
"""

from django.contrib.auth.models import User


def make_player():
    """Helper method for creating a User who is the player"""
    player, just_created = User.objects.get_or_create(username='player')
    return player
