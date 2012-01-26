"""
Tests for attributes on Mission objects.
"""

import unittest

from mmolfg.missions.models import Mission


class TestMissionModel(unittest.TestCase):
    """Ensure attributes and methods on Mission."""

    def test_mission_type_default(self):
        """Each mission should start with a default alert type."""
        mission = Mission()
        self.assertEqual(1, mission.mission_type)

    def test_mission_create_mission_type(self):
        """You should be able to specify the mission type when created."""
        mission = Mission(mission_type=0)
        self.assertEqual(0, mission.mission_type)

    def test_mission_update_mission_type(self):
        """You should be able to update a Mission's mission_type."""
        mission = Mission()
        mission.mission_type = 3
        self.assertEqual(3, mission.mission_type)
