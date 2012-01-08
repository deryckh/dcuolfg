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
        toon = Character(name=name, server=0)
        with self.assertRaises(ValidationError) as err:
            toon.full_clean()
        expected_message = (
            'Ensure this value has at most 75 characters '
            '(it has 80).')
        message_list = err.exception.message_dict.get('name')
        self.assertEqual(expected_message, message_list[0])

    def test_character_name_blank(self):
        """Characters cannot be created with blank names."""
        toon = Character(name='', server=0)
        with self.assertRaises(ValidationError) as err:
            toon.full_clean()
        expected_message = 'This field cannot be blank.'
        message_list = err.exception.message_dict.get('name')
        self.assertEqual(expected_message, message_list[0])

    def test_character_name_allows_space(self):
        """Characters can have names with spaces in them."""
        name = 'Captain DjangoHacker'
        toon = Character(name=name, server=0)
        toon.full_clean()
        self.assertEqual(name, toon.name)

    def test_server(self):
        """Each Character lives on a server."""
        server = 0
        toon = Character(name='foobar', server=server)
        self.assertEqual(server, toon.server)

    def test_server_required(self):
        """You should not be able to create a chracter without a server."""
        toon = Character(name='foobar')
        with self.assertRaises(ValidationError) as err:
            toon.full_clean()
        expected_message = 'This field cannot be null.'
        message_list = err.exception.message_dict.get('server')
        self.assertEqual(expected_message, message_list[0])
