"""
Tests for Profile objects in mmolfg.
"""

import unittest

from mmolfg.accounts.models import Profile


class TestProfileModel(unittest.TestCase):
    """Tests to ensure expected attributes for Profile modules."""

    def test_profile_without_real_name(self):
        """Profile can exist without a real name."""
        profile = Profile()
        self.assertEqual('', profile.real_name)

    def test_profile_real_name(self):
        """Profile should be able to add a real name."""
        profile = Profile()
        profile.real_name = 'Deryck Hodge'
        self.assertEqual('Deryck Hodge', profile.real_name)
