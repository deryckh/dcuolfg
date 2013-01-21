# Copyright 2012 Deryck Hodge.  This software is licensed under the
# GNU Lesser General Public License version 3 (see the file LICENSE).

"""
Test suite for characters app in dcuolfg.
"""

import unittest

from dcuolfg.characters.tests.characters import TestCharacterModel
from dcuolfg.characters.tests.lfg import TestLFGRequest
from dcuolfg.characters.tests.votes import TestCharacterVotes


UNIT_TESTS = (
    TestCharacterModel,
    TestCharacterVotes,
    TestLFGRequest,
)


def suite():
    """The test suite of all character tests."""
    test_suite = unittest.TestSuite()
    for ut in UNIT_TESTS:
        test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(ut))
    return test_suite
