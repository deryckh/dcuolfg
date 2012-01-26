"""
Tests for Character objects in mmolfg.
"""

import datetime
import unittest

from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField

from mmolfg.characters.models import Character
from mmolfg.characters.tests.utils import make_player


class TestCharacterModel(unittest.TestCase):
    """Tests to ensure expected attributes for Character objects."""

    def test_player(self):
        """Each Character should have a player attribute."""
        fred = User(username='fred')
        toon = Character(name='Gazorbeam', server=0, player=fred)
        self.assertEqual(fred, toon.player)

    def test_player_has_chracters(self):
        """Every user who is a player should have characters."""
        player = make_player()
        toon = Character(name='funbar foo', server=0, player=player)
        another_toon = Character(name='flexbar fofo', server=0, player=player)
        expected_toons = [toon, another_toon]
        actual_toons = list(player.characters.all())
        self.assertEqual(expected_toons.sort(), actual_toons.sort())

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
        player = make_player()
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
        player = make_player()
        toon = Character(name='', server=0, player=player)
        with self.assertRaises(ValidationError) as err:
            toon.full_clean()
        expected_message = 'This field cannot be blank.'
        message_list = err.exception.message_dict.get('name')
        self.assertEqual(expected_message, message_list[0])

    def test_character_name_allows_space(self):
        """Characters can have names with spaces in them."""
        name = 'Captain DjangoHacker'
        player = make_player()
        toon = Character(
            name=name, server=0, player=player, role=0, powerset=0)
        toon.full_clean()
        self.assertEqual(name, toon.name)

    def test_server(self):
        """Each Character lives on a server."""
        server = 0
        toon = Character(name='foobar', server=server)
        self.assertEqual(server, toon.server)
        self.assertEqual('USPS3', toon.get_server_display())

    def test_server_required(self):
        """You should not be able to create a chracter without a server."""
        player = make_player()
        toon = Character(name='foobar', player=player)
        with self.assertRaises(ValidationError) as err:
            toon.full_clean()
        expected_message = 'This field cannot be null.'
        message_list = err.exception.message_dict.get('server')
        self.assertEqual(expected_message, message_list[0])

    def test_get_server_value(self):
        """Characters have a get_server_value method."""
        toon = Character(name='GoHomeBuddy')
        self.assertEqual(0, toon.get_server_value('USPS3'))

    def test_get_server_value_none(self):
        """Character.get_server_value will return None for unknown servers."""
        toon = Character(name='YourBiggestFan')
        self.assertEqual(None, toon.get_server_value('jhdbhjbdehjb'))

    def test_role(self):
        """Each Character has a role when created."""
        toon = Character(name='NewHero', role=0)
        self.assertEqual(0, toon.role)

    def test_role_required(self):
        """You should not be able to create a character without a role."""
        player = make_player()
        toon = Character(name='foobar', player=player)
        with self.assertRaises(ValidationError) as err:
            toon.full_clean()
        expected_message = 'This field cannot be null.'
        message_list = err.exception.message_dict.get('role')
        self.assertEqual(expected_message, message_list[0])

    def test_powerset(self):
        """Characters have a powerset attribute when created."""
        toon = Character(name='SomeToon', powerset=0)
        self.assertEqual(0, toon.powerset)

    def test_powerset_required(self):
        """You should not be able to create a Character without a powerset."""
        player = make_player()
        toon = Character(name='foobar', player=player)
        with self.assertRaises(ValidationError) as err:
            toon.full_clean()
        expected_message = 'This field cannot be null.'
        message_list = err.exception.message_dict.get('powerset')
        self.assertEqual(expected_message, message_list[0])

    def test_character_without_description(self):
        """Characters can be created without a description."""
        toon = Character()
        self.assertEqual('', toon.description)

    def test_description(self):
        """A Character can have a description."""
        player = make_player()
        toon = Character(name='My SuperDude', server=0, player=player)
        description = """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
            enim ad minim veniam, quis nostrud exercitation ullamco."""
        toon.description = description
        self.assertEqual(description, toon.description)

    def test_starting_level(self):
        """A Character starts with a level of 1."""
        toon = Character(name='FriendlyHeroToon')
        self.assertEqual(1, toon.level)

    def test_level_update(self):
        """A Character can update his or her level."""
        toon = Character(name='EvilVillainToon')
        toon.level = 30
        self.assertEqual(30, toon.level)

    def test_level_cap(self):
        """A Character has a max level of 30."""
        player = make_player()
        toon = Character(name='FakeToon', player=player, server=0)
        toon.level = 31
        with self.assertRaises(ValidationError) as err:
            toon.full_clean()
        expected_message = 'Ensure this value is less than or equal to 30.'
        message_list = err.exception.message_dict.get('level')
        self.assertEqual(expected_message, message_list[0])

    def test_level_min(self):
        """A Character cannot have a negative level."""
        player = make_player()
        toon = Character(name='UnrealNegativeHero', player=player, server=0)
        toon.level = -1
        with self.assertRaises(ValidationError) as err:
            toon.full_clean()
        expected_message = 'Ensure this value is greater than or equal to 0.'
        message_list = err.exception.message_dict.get('level')
        self.assertEqual(expected_message, message_list[0])

    def test_starting_combat_rating(self):
        """A Character starts with a combat_rating of 0."""
        toon = Character(name='SomeToon')
        self.assertEqual(0, toon.combat_rating)

    def test_combat_rating_update(self):
        """A Character can have a combat_rating."""
        toon = Character(name='Someone')
        toon.combat_rating = 64
        self.assertEqual(64, toon.combat_rating)

    def test_starting_skill_points(self):
        """A Character starts with 0 skill points."""
        toon = Character(name='SomeToon')
        self.assertEqual(0, toon.skill_points)

    def test_skill_points_update(self):
        """A Character can track his skill points."""
        toon = Character(name='SomeToon')
        toon.skill_points = 101
        self.assertEqual(101, toon.skill_points)

    def test_is_main_default(self):
        """A Character should not be set is_main by default."""
        toon = Character()
        self.assertFalse(toon.is_main)

    def test_is_main_update(self):
        """You should be able to set a Character as your main toon."""
        toon = Character()
        toon.is_main = True
        self.assertTrue(toon.is_main)

    def test_character_without_image(self):
        """Characters can be created without image info."""
        toon = Character()
        self.assertEqual('', toon.image)

    def test_character_image_update(self):
        """Characters should be able to specify an image.

        This test is for completeness sake.  Most of this is
        hidden away behind the model, admin, or form interactions.
        """
        toon = Character(name='ToonWithImage')
        img = ImageField('toon_with_image.png')
        toon.image = img
        self.assertEqual(img, toon.image)

    def test_date_added(self):
        """A character should have a date_added attribute when added."""
        toon = Character(name='SomeoneAdded')
        self.assertIsInstance(toon.date_added, datetime.datetime)

    def test_date_added_updated(self):
        """You should be able to update the date added."""
        toon = Character(name='SomeToon')
        older_date = datetime.datetime.now() - datetime.timedelta(7)
        toon.date_added = older_date
        self.assertEqual(older_date, toon.date_added)

    def test_date_updated(self):
        """A Character should have a date_updated when created."""
        toon = Character(name='MeToon')
        self.assertIsInstance(toon.date_updated, datetime.datetime)

    def test_date_updated_changed(self):
        """You should be able to update Character.date_updated."""
        toon = Character(name='GazerBeam')
        new_date = datetime.datetime.now() + datetime.timedelta(14)
        toon.date_updated = new_date
        self.assertEqual(new_date, toon.date_updated)
