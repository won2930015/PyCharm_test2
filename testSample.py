import unittest

from Solver import Solver


class MyTestCase(unittest.TestCase):


    def test_negative_discr(self):
        s = Solver()
        # self.assertRaises(Exception)
        self.assertRaises(Exception, s.demo, 2, 1, 2)

    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
