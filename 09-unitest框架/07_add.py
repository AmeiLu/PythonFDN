import unittest

from py06_test_add import TestAdd

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestAdd))

unittest.TextTestRunner().run(suite)