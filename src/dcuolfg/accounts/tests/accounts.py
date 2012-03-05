# Copyright 2012 Deryck Hodge.  This software is licensed under the
# GNU Lesser General Public License version 3 (see the file LICENSE).

"""
Tests for Profile objects in dcuolfg.
"""

import unittest

from django.core.exceptions import ValidationError
from sorl.thumbnail import ImageField

from dcuolfg.accounts.models import Profile
from dcuolfg.characters.models import Character


class TestProfileModel(unittest.TestCase):
    """Tests to ensure expected attributes for Profile modules."""

    def test_profile_without_real_name(self):
        """Profile can exist without a real name."""
        profile = Profile()
        self.assertEqual('', profile.real_name)

    def test_profile_update_real_name(self):
        """Profile should be able to add a real name."""
        profile = Profile()
        profile.real_name = 'Deryck Hodge'
        self.assertEqual('Deryck Hodge', profile.real_name)

    def test_profile_without_about(self):
        """Profile should start without about text."""
        profile = Profile()
        self.assertEqual('', profile.about)

    def test_profile_update_about(self):
        """You should be able to update a Profile about text."""
        profile = Profile()
        about = """Lorem ipsum dolor sit amet, consectetur adipisicing
            elit, sed do eiusmod tempor incididunt ut labore et dolore magna
            aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco
            laboris nisi ut aliquip ex ea commodo consequat."""
        profile.about = about
        self.assertEqual(about, profile.about)

    def test_profile_without_location(self):
        """Profile should start without a location."""
        profile = Profile()
        self.assertEqual('', profile.location)

    def test_profile_update_location(self):
        """You should be able to update a Profile's location."""
        profile = Profile()
        profile.location = 'Somewhere, Somestate'
        self.assertEqual('Somewhere, Somestate', profile.location)

    def test_profile_without_web(self):
        """Profile should start without web filled in."""
        profile = Profile()
        self.assertEqual('', profile.web)

    def test_profile_update_web(self):
        """You should be able to update web for a Profile."""
        profile = Profile()
        profile.web = 'http://example.com/'
        self.assertEqual('http://example.com/', profile.web)

    def test_profile_web_validation(self):
        """Profile.web should be a real URL.

        Even partial URLs are not allowed.
        """
        profile = Profile()
        profile.web = 'foobar.com'
        with self.assertRaises(ValidationError) as err:
            profile.full_clean()
        expected_message = 'Enter a valid value.'
        message_list = err.exception.message_dict.get('web')
        self.assertEqual(expected_message, message_list[0])

    def test_profile_without_image(self):
        """Profile should be created without image info."""
        profile = Profile()
        self.assertEqual('', profile.image)

    def test_character_update_image(self):
        """Profile should be able to specify an image.

        This test is for completeness sake.  Most of this is
        hidden away behind the model, admin, or form interactions.
        """
        profile = Profile()
        img = ImageField('profile_image.png')
        profile.image = img
        self.assertEqual(img, profile.image)

    def test_profile_without_browsing_as(self):
        """Profile should not set browsing_as when created."""
        profile = Profile()
        self.assertIsNone(profile.browsing_as)

    def test_profile_update_browsing_as(self):
        """You should be able to update browsing_as for a Profile."""
        profile = Profile()
        character = Character()
        profile.browsing_as = character
        self.assertEqual(character, profile.browsing_as)
