"""
Tests for Character objects in mmolfg.
"""

import unittest

from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from mmolfg.characters.models import Character


class TestCharacterAttributes(unittest.TestCase):
    """Tests to ensure expected attributes for Character objects."""

    def make_player(self):
        """Helper method for creating a User who is the player"""
        player, just_created = User.objects.get_or_create(username='player')
        return player

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
        player = self.make_player()
        toon = Character(name=name, server=0, player=player)
        with self.assertRaises(ValidationError) as err:
            toon.full_clean()
        expected_message = (
            'Ensure this value has at most 75 characters '
            '(it has 80).')
        message_list = err.exception.message_dict.get('name')
        self.assertEqual(expected_message, message_list[0])

    def test_character_name_blank(self):
        """Characters cannot be created with blank names."""
        player = self.make_player()
        toon = Character(name='', server=0, player=player)
        with self.assertRaises(ValidationError) as err:
            toon.full_clean()
        expected_message = 'This field cannot be blank.'
        message_list = err.exception.message_dict.get('name')
        self.assertEqual(expected_message, message_list[0])

    def test_character_name_allows_space(self):
        """Characters can have names with spaces in them."""
        name = 'Captain DjangoHacker'
        player = self.make_player()
        toon = Character(name=name, server=0, player=player)
        toon.full_clean()
        self.assertEqual(name, toon.name)

    def test_server(self):
        """Each Character lives on a server."""
        server = 0
        toon = Character(name='foobar', server=server)
        self.assertEqual(server, toon.server)

    def test_server_required(self):
        """You should not be able to create a chracter without a server."""
        player = self.make_player()
        toon = Character(name='foobar', player=player)
        with self.assertRaises(ValidationError) as err:
            toon.full_clean()
        expected_message = 'This field cannot be null.'
        message_list = err.exception.message_dict.get('server')
        self.assertEqual(expected_message, message_list[0])

    def test_player(self):
        """Each Character should have a player attribute."""
        fred = User(username='fred')
        toon = Character(name='Gazorbeam', server=0, player=fred)
        self.assertEqual(fred, toon.player)

    def test_player_has_chracters(self):
        """Every user who is a player should have characters."""
        player = self.make_player()
        toon = Character(name='funbar foo', server=0, player=player)
        another_toon = Character(name='flexbar fofo', server=0, player=player)
        expected_toons = [toon, another_toon]
        actual_toons = list(player.characters.all())
        self.assertEqual(expected_toons.sort(), actual_toons.sort())

    def test_description(self):
        """A Character can have a description."""
        player = self.make_player()
        toon = Character(name='My SuperDude', server=0, player=player)
        description = """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
            enim ad minim veniam, quis nostrud exercitation ullamco."""
        toon.description = description
        toon.save()
        updated_toon = Character.objects.filter(name='My SuperDude')[0]
        self.assertEqual(description, updated_toon.description)
