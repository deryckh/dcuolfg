"""
Tests for attributes on Mission objects.
"""

import unittest

from django.core.exceptions import ValidationError
from sorl.thumbnail import ImageField

from mmolfg.missions.models import (
    Location,
    Mission,
)


class TestMissionModel(unittest.TestCase):
    """Ensure attributes and methods on Mission."""

    def test_mission_type_default(self):
        """Each mission should start with a default alert type."""
        mission = Mission()
        self.assertEqual(1, mission.mission_type)
        self.assertEqual('Alert', mission.get_mission_type_display())

    def test_mission_create_mission_type(self):
        """You should be able to specify the mission type when created."""
        mission = Mission(mission_type=0)
        self.assertEqual(0, mission.mission_type)

    def test_mission_update_mission_type(self):
        """You should be able to update a Mission's mission_type."""
        mission = Mission()
        mission.mission_type = 3
        self.assertEqual(3, mission.mission_type)

    def test_mission_without_mode(self):
        """Mission should not have a mode when created."""
        mission = Mission()
        self.assertIsNone(mission.mode)

    def test_mission_update_mode(self):
        """You should be able to update the mode of a mission."""
        mission = Mission()
        mission.mode = 1
        self.assertEqual(1, mission.mode)
        self.assertEqual('T1', mission.get_mode_display())

    def test_mission_name(self):
        """A Mission should have a name when created."""
        mission = Mission(name='Area 51')
        self.assertEqual('Area 51', mission.name)

    def test_mission_name_required(self):
        """You should not be able to create a Mission without a name."""
        mission = Mission()
        with self.assertRaises(ValidationError) as err:
            mission.full_clean()
        expected_message = 'This field cannot be blank.'
        message_list = err.exception.message_dict.get('name')
        self.assertEqual(expected_message, message_list[0])

    def test_mission_location(self):
        """A Mission should have a location when created."""
        location = Location(name='Smallville')
        mission = Mission(location=location)
        self.assertEqual(location, mission.location)

    def test_mission_location_has_missions(self):
        """Locations should have a reference back to related missions."""
        location = Location(name='Smallville')
        location.save()
        mission = Mission(location=location)
        mission.save()
        expected_missions = [mission]
        actual_missions = list(location.missions.all())
        self.assertEqual(expected_missions, actual_missions)

    def test_mission_location_without_image(self):
        """A Location should be created without an image."""
        location = Location()
        self.assertEqual('', location.image)

    def test_mission_location_update_image(self):
        """Locations should be able to specify an image.

        This test is for completeness sake.  Most of this is
        hidden away behind the model, admin, or form interactions.
        """
        location = Location()
        img = ImageField('location_image.png')
        location.image = img
        self.assertEqual(img, location.image)

    def test_mission_num_players_default(self):
        """Mission objects are created for 4 players by default."""
        mission = Mission()
        self.assertEqual(4, mission.num_players)
        self.assertEqual('4', mission.get_num_players_display())

    def test_mission_update_num_players(self):
        """You should be able to update num_players for a Mission."""
        mission = Mission()
        mission.num_players = 8
        self.assertEqual(8, mission.num_players)

    def test_mission_num_players_possible(self):
        """You should not be able to specify arbitrary num_players."""
        mission = Mission()
        mission.num_players = 33
        with self.assertRaises(ValidationError) as err:
            mission.full_clean()
        expected_message = 'Value 33 is not a valid choice.'
        message_list = err.exception.message_dict.get('num_players')
        self.assertEqual(expected_message, message_list[0])
