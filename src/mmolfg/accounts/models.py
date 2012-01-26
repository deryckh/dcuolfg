"""
Models for user account profiles.
"""

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import ImageField

from mmolfg.characters.models import Character


class Profile(models.Model):
    """Profile module for Users."""

    user = models.ForeignKey(User, verbose_name=_('user'))
    real_name = models.CharField(_('real name'), max_length=75, blank=True)
    about = models.TextField(_('about'), blank=True)
    location = models.CharField(_('location'), max_length=100, blank=True)
    web = models.URLField(_('web'), blank=True, verify_exists=False)
    image = ImageField(
        _('image'), upload_to='img/profiles/%Y/%m/%d', blank=True)
    browsing_as = models.ForeignKey(
        Character, blank=True, null=True, verbose_name=_('browsing as'))

    class Meta:
        """Meta options for Profile."""
        db_table = 'user_profile'

    def __unicode__(self):
        """Profile name returned by unicode."""
        return u'Profile for: %s' % self.user.username
