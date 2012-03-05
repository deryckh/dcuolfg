# Copyright 2012 Deryck Hodge.  This software is licensed under the
# GNU Lesser General Public License version 3 (see the file LICENSE).

"""
Tests for voting system for Characters.
"""

import unittest

from dcuolfg.characters.models import (
    Character,
    CharacterVote,
)
from dcuolfg.characters.tests.utils import make_player


class TestCharacterVotes(unittest.TestCase):
    """Tests to ensure votes for and by Characters work as expected."""

    def test_character_votes(self):
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

    def test_character_positive_votes_starting_count(self):
        """Each Character starts with 0 positive votes from CharacterVote."""
        player = make_player()
        toon = Character(
            name='AMainToon', server=0, role=0, powerset=0, player=player)
        toon.save()
        self.assertEqual(0, toon.positive_votes)

    def test_character_positive_votes_count_updates(self):
        """Each Character's positive_votes updates after new CharacterVote."""
        player = make_player()
        toon = Character(
            name='BMainToon', server=0, role=0, powerset=0, player=player)
        toon.save()
        alt_toon = Character(
            name='AAltToon', server=0, role=1, powerset=1, player=player)
        alt_toon.save()
        vote = CharacterVote(character=alt_toon, voter=toon, vote=1)
        vote.save()
        self.assertEqual(1, alt_toon.positive_votes)

    def test_character_negative_votes_starting_count(self):
        """Each Character starst with 0 negative votes from CharacterVote."""
        player = make_player()
        toon = Character(
            name='CMainToon', server=0, role=0, powerset=0, player=player)
        toon.save()
        self.assertEqual(0, toon.negative_votes)

    def test_character_negative_votes_count_updates(self):
        """Each Character's negative_votes updates after new CharacterVote."""
        player = make_player()
        toon = Character(
            name='DMainToon', server=0, role=0, powerset=0, player=player)
        toon.save()
        alt_toon = Character(
            name='BAltToon', server=0, role=1, powerset=1, player=player)
        alt_toon.save()
        vote = CharacterVote(character=alt_toon, voter=toon, vote=0)
        vote.save()
        self.assertEqual(1, alt_toon.negative_votes)
