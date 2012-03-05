"""
Test suite for missions app in DCUO LFG.
"""

import unittest

from mmolfg.missions.tests.missions import TestMissionModel

UNIT_TESTS = (
    TestMissionModel,
)


def suite():
    """The test suite of all missions tests."""
    test_suite = unittest.TestSuite()
    for ut in UNIT_TESTS:
        test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(ut))
    return test_suite
