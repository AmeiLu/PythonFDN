import unittest

from test_01_test_login import TestLogin

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))

runner = unittest.TextTestRunner()
runner.run(suite)