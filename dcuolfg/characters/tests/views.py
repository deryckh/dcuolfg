# Copyright 2012-2013 Deryck Hodge.  This software is licensed under the
# GNU Lesser General Public License version 3 (see the file LICENSE).

"""
Tests for Character view functions.
"""

import unittest

from django.test.client import Client

from dcuolfg.characters.views import _get_server_value_from_name


class TestCharacterViewFunctions(unittest.TestCase):
    """Tests for top-level view functions in the character module."""

    def test_get_server_value_from_name_returns_value(self):
        """_get_server_value_from_name should return the correct value."""
        self.assertEqual(0, _get_server_value_from_name('USPS3'))

    def test_character_get_server_value_none(self):
        """_get_server_value_from_name returns None for unknown servers."""
        self.assertEqual(None, _get_server_value_from_name('jhdbhjbdehjb'))


class TestCharacterBrowsing(unittest.TestCase):
    """Tests for browsing characters on the site."""

    def test_unknown_character_profile_404(self):
        """Browsing to an unknown character should 404."""
        browser = Client()
        response = browser.get('/characters/USPS3/ThisToonDoesNotExist/')
        self.assertEqual(404, response.status_code)
