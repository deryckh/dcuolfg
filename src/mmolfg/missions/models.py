"""
Models for missions in DCUO LFG.
"""

from django.db import models
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import ImageField


class Location(models.Model):
    """Mission Location object."""

    name = models.CharField(max_length=100)
    image = ImageField(
        _('image'), upload_to='img/locations/%Y/%m/%d', blank=True)

    class Meta:
        """Meta options for Location objects."""
        db_table = 'mission_location'

    def __unicode__(self):
        """unicode representation for Location"""
        return self.name


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
        (7, 'Event'),
    )

    MISSION_MODE_CHOICES = (
        (0, 'Normal'),
        (1, 'T1'),
        (2, 'T2'),
    )

    MISSION_NUM_PLAYER_CHOICES = (
        (2, '2'),
        (4, '4'),
        (5, '5'),
        (8, '8'),
    )

    mission_type = models.IntegerField(
        _('mission type'), choices=MISSION_TYPE_CHOICES, default=1)
    mode = models.IntegerField(
        _('mode'), blank=True, null=True, choices=MISSION_MODE_CHOICES)
    name = models.CharField(_('name'), max_length=100)
    short_name = models.CharField(_('short name'), max_length=25)
    location = models.ForeignKey(
        Location, verbose_name=_('location'), related_name='missions')
    num_players = models.IntegerField(
        _('Number of players'), choices=MISSION_NUM_PLAYER_CHOICES, default=4)
    featured = models.BooleanField(_('featured'), default=False)

    class Meta():
        """Meta options for Mission."""
        db_table = 'mission'

    def __unicode__(self):
        """unicode representation of a Mission."""
        mission = self.get_mission_type_display()
        name = self.name
        location_name = self.location.name
        if name != location_name:
            full_name = '%s: %s' % (self.location.name, self.name)
        else:
            full_name = name
        if self.mode is not None:
            return u'%s %s %s' % (full_name, self.get_mode_display(), mission)
        return u'%s %s' % (full_name, mission)
