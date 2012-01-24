"""
Test suite for characters app in mmolfg.
"""

import unittest

from mmolfg.characters.tests.characters import TestCharacterModel
from mmolfg.characters.tests.votes import TestCharacterVotes

UNIT_TESTS = (
    TestCharacterModel,
    TestCharacterVotes,
)


def suite():
    """The test suite of all character tests."""
    test_suite = unittest.TestSuite()
    for ut in UNIT_TESTS:
        test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(ut))
    return test_suite
