# Copyright 2012-2013 Deryck Hodge.  This software is licensed under the
# GNU Lesser General Public License version 3 (see the file LICENSE).

"""
Models for characters in dcuolfg.
"""

import datetime

from django.contrib.auth.models import User
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
)
from django.db import models
from django.utils.translation import ugettext_lazy as _

from dcuolfg.characters.managers import CharacterManager
from dcuolfg.missions.models import Mission


class Character(models.Model):
    """Characters used by Players in DCUO."""

    CHARACTER_SERVER_CHOICES = (
        (0, 'USPS3'),
        (1, 'USPC'),
        (2, 'EUPS3'),
        (3, 'EUPC'),
    )

    CHARACTER_ROLE_CHOICES = (
        (0, 'DPS'),
        (1, 'Controller'),
        (2, 'Healer'),
        (3, 'Tank'),
    )

    CHARACTER_POWERSET_CHOICES = (
        (0, 'Fire'),
        (1, 'Ice'),
        (2, 'Gadgets'),
        (3, 'Mental'),
        (4, 'Light'),
        (5, 'Socery'),
        (6, 'Nature'),
        (7, 'Electricity'),
    )

    player = models.ForeignKey(
        User, related_name='characters', verbose_name=_('player'))
    name = models.CharField(_('name'), max_length=75)
    server = models.IntegerField(
        _('server'), choices=CHARACTER_SERVER_CHOICES)
    role = models.IntegerField(_('role'), choices=CHARACTER_ROLE_CHOICES)
    powerset = models.IntegerField(
        _('powerset'), choices=CHARACTER_POWERSET_CHOICES)
    description = models.TextField(_('description'), blank=True,
        help_text=_('A short blurb describing your toon.'))
    level = models.IntegerField(
        _('level'), blank=True, null=True, default=1,
        validators=[MinValueValidator(0), MaxValueValidator(30)])
    combat_rating = models.IntegerField(
        _('combat_rating'), null=True, blank=True, default=0)
    skill_points = models.IntegerField(
        _('skill_points'), blank=True, null=True, default=0)
    league = models.CharField(_('league'), blank=True, max_length=100)
    image = models.ImageField(
        _('image'), upload_to='img/characters/%Y/%m/%d', blank=True)
    is_main = models.BooleanField(_('is_main'), default=False)
    lfg = models.BooleanField(_('lfg'), default=False)

    # The dates make use of auto_now and auto_now_add options, but
    # also include a "default" value.  This is so that Character objects
    # work sanely without having to call save on them.
    date_added = models.DateTimeField(
        _('date_added'), auto_now_add=True, auto_now=False,
        default=datetime.datetime.now)
    date_updated = models.DateTimeField(
        _('date_updated'), auto_now_add=True, auto_now=True,
        default=datetime.datetime.now)

    # Denormalized vote counts, to make it easier and faster
    # to get at the CharacterVote data.
    positive_votes = models.PositiveIntegerField(
        _('positive_votes'), default=0)
    negative_votes = models.PositiveIntegerField(
        _('negative_votes'), default=0)

    objects = CharacterManager()

    class Meta:
        """Metadata for Character model."""
        unique_together = ('server', 'name')
        db_table = 'character'
        get_latest_by = 'date_added'

    def __unicode__(self):
        """Used to describe each object in admin."""
        return u'%s: %s' % (self.get_server_display(), self.name)


class CharacterVote(models.Model):
    """Votes for or against a Character."""

    CHARACTER_VOTE_CHOICES = (
        (0, '-1'),
        (1, '+1'),
    )

    character = models.ForeignKey(
        Character, related_name='votes_for', verbose_name=_('character'))
    voter = models.ForeignKey(
        Character, related_name='votes_by', verbose_name=_('voter'))
    vote = models.IntegerField(_('vote'), choices=CHARACTER_VOTE_CHOICES)

    class Meta:
        """Metadata for CharacterVote model."""
        db_table = 'character_vote'

    def save(self, *args, **kwargs):
        """Override save to handle vote counting on Character."""
        super(CharacterVote, self).save(*args, **kwargs)
        if self.vote == 0:
            self.character.negative_votes += 1
        else:
            self.character.positive_votes += 1
        self.character.save()


class LFGRequest(models.Model):
    """The main object for tracking what Characters are LFG for."""

    LFG_CONTACT_CHOICES = (
        (0, 'In-game tell before invite.'),
        (1, 'Blind invites are fine.'),
        (2, 'See description for more details.'),
    )

    character = models.ForeignKey(
        Character, verbose_name=_('character'), related_name='requests')
    mission = models.ForeignKey(
        Mission, verbose_name=_('mission'), related_name='requests')
    description = models.TextField(_('description'), blank=True)
    contact_info = models.IntegerField(default=0, choices=LFG_CONTACT_CHOICES)

    class Meta:
        """Meta options for LFGRequest."""
        db_table = 'lfg_request'
        verbose_name = 'LFG Request'
        verbose_name_plural = 'LFG Requests'

    def __unicode__(self):
        """unicode representation of LFGRequest."""
        return u'LFG %s, for %s' % (self.character, self.mission)
