# Copyright 2012 Deryck Hodge.  This software is licensed under the
# GNU Lesser General Public License version 3 (see the file LICENSE).

"""
Test suite for accounts app in dcuolfg.
"""

import unittest

from dcuolfg.accounts.tests.accounts import TestProfileModel

UNIT_TESTS = (
    TestProfileModel,
)


def suite():
    """The test suite of all accounts tests."""
    test_suite = unittest.TestSuite()
    for ut in UNIT_TESTS:
        test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(ut))
    return test_suite
