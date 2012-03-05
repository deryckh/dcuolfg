"""
Tests for LFG-related Character objects.
"""

import unittest

from mmolfg.characters.models import (
    Character,
    LFGRequest,
)
from mmolfg.characters.tests.utils import make_player
from mmolfg.missions.models import (
    Location,
    Mission,
)


class TestLFGRequest(unittest.TestCase):
    """Test attributes of an LFGRequest."""

    def test_lfg_request_character(self):
        """An LFGRequest should be created with a Character."""
        toon = Character()
        lfg = LFGRequest(character=toon)
        self.assertEqual(toon, lfg.character)

    def test_lfg_request_update_character(self):
        """You should be able to update the Character for an LFGRequest."""
        toon = Character()
        alt = Character()
        lfg = LFGRequest(character=toon)
        lfg.character = alt
        self.assertIsNot(toon, alt)
        self.assertEqual(alt, lfg.character)

    def test_lfg_request_mission(self):
        """An LFGRequest should be created with a Mission."""
        mission = Mission()
        lfg = LFGRequest(mission=mission)
        self.assertEqual(mission, lfg.mission)

    def test_lfg_request_update_mission(self):
        """You should be able to update the mission of an LFGRequest."""
        mission = Mission()
        alt_mission = Mission()
        lfg = LFGRequest(mission=mission)
        lfg.mission = alt_mission
        self.assertIsNot(alt_mission, mission)
        self.assertEqual(alt_mission, lfg.mission)

    def test_lfg_request_without_description(self):
        """You should not have to specify a description on an LFGRequest."""
        lfg = LFGRequest()
        self.assertEqual('', lfg.description)

    def test_lfg_request_update_description(self):
        """You should be able to update the description on an LFGRequest."""
        lfg = LFGRequest()
        description = """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit,
            sed do eiusmod tempor incididunt ut labore et dolore magna
            aliqua. Ut enim ad minim veniam, quis nostrud exercitation.
        """
        lfg.description = description
        self.assertEqual(description, lfg.description)

    def test_lfg_request_contact_info_default(self):
        """LFGRequests should have a default contact_info."""
        lfg = LFGRequest()
        self.assertEqual(0, lfg.contact_info)
        self.assertEqual(
            'Send in-game tell before sending invite.',
            lfg.get_contact_info_display())

    def test_lfg_request_update_contact_info(self):
        """You should be able to update contact_info for an LFGRequest."""
        lfg = LFGRequest()
        lfg.contact_info = 1
        self.assertEqual(1, lfg.contact_info)

    def test_character_has_lfg_requests(self):
        """A Character should be associated with his/her LFGRequests."""
        player = make_player()
        toon = Character(
            name='Duskstrike', server=0, role=0, powerset=0, player=player)
        toon.save()
        location = Location(name='Somewhere')
        location.save()
        mission = Mission(name='FooMission', location=location)
        mission.save()
        lfg = LFGRequest(character=toon, mission=mission)
        lfg.save()
        expected_requests = [lfg]
        actual_requests = list(toon.requests.all())
        self.assertEqual(expected_requests, actual_requests)

    def test_mission_has_lfg_requests(self):
        """A Mission should be associated with its LFGRequests."""
        player = make_player()
        toon = Character(
            name='Scarlet Letter', server=0, role=0, powerset=0, player=player)
        toon.save()
        location = Location(name='Someplace')
        location.save()
        mission = Mission(name='FooMissionBar', location=location)
        mission.save()
        lfg = LFGRequest(character=toon, mission=mission)
        lfg.save()
        expected_requests = [lfg]
        actual_requests = list(mission.requests.all())
        self.assertEqual(expected_requests, actual_requests)
