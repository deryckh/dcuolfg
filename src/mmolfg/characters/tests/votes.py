"""
Tests for voting system for Characters.
"""

import unittest

from mmolfg.characters.models import (
    Character,
    CharacterVote,
)
from mmolfg.characters.tests.utils import make_player


class TestCharacterVotes(unittest.TestCase):
    """Tests to ensure votes for and by Characters work as expected."""

    def test_character_can_vote(self):
        """One character can create a positive vote for another."""
        player = make_player()
        toon = Character(
            name='MyMainToon', server=0, role=0, powerset=0, player=player)
        toon.save()
        alt_toon = Character(
            name='MyAltToon', server=0, role=1, powerset=1, player=player)
        alt_toon.save()
        vote = CharacterVote(character=alt_toon, voter=toon, vote=1)
        vote.save()
        # First, confirm expected behavior for the person voted for.
        votes_for = alt_toon.votes_for.all()
        self.assertIn(vote, votes_for)
        self.assertEqual(1, votes_for[0].vote)
        self.assertEqual(alt_toon, votes_for[0].character)
        # Finally, confirm expected behavior for the person who voted.
        votes_by = toon.votes_by.all()
        self.assertIn(vote, votes_by)
        self.assertEqual(1, votes_by[0].vote)
        self.assertEqual(toon, votes_by[0].voter)
