"""
Tests for Character objects in mmolfg.
"""

import unittest

from django.core.exceptions import ValidationError

from mmolfg.characters.models import Character


class TestCharacterAttributes(unittest.TestCase):
    """Tests to ensure expected attributes for Character objects.

    Do not call save or use Character.objects.create (which calls
    save).  This avoids saving to DB, since we're just checking
    the Character object's API.
    """

    def test_character_name(self):
        """Each Character instance should have a name attribute."""
        name = 'superdoopertoon'
        toon = Character(name=name)
        self.assertEqual(name, toon.name)

    def test_character_name_length(self):
        """Character names cannot be over 75 characters long."""
        name = (
            'thisisareaallylongname'
            'fhenjnndeukabandnjndehbdehbhdbehbdehbhdbjndejnjdnejndjendj')
        toon = Character(name=name)
        self.assertRaises(ValidationError, toon.full_clean)

    def test_character_name_blank(self):
        """Characters cannot be created with blank names."""
        toon = Character(name='')
        self.assertRaises(ValidationError, toon.full_clean)
