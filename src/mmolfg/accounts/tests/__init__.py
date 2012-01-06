"""
Test suite for accounts app in mmolfg.
"""

import unittest

from mmolfg.accounts.tests.accounts import TestBaseTest

UNIT_TESTS = (
    TestBaseTest,
)


def suite():
    """The test suite of all accounts tests."""
    test_suite = unittest.TestSuite()
    for ut in UNIT_TESTS:
        test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(ut))
    return test_suite
