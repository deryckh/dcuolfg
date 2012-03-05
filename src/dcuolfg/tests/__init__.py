"""
Test suite for mmolfg.
"""

import unittest

from mmolfg.characters.tests.characters import TestBaseTest

UNIT_TESTS = (
    TestBaseTest,
)

def suite():
    test_suite = unittest.TestSuite()
    for ut in UNIT_TESTS:
        test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(ut))
    return test_suite
