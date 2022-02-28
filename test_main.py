from main import *
import unittest


class TestChange(unittest.TestCase):
    def test_change(self):
        self.assertAlmostEqual(give_change([5, 10, 5, 50, 10, 20, 100, 200, 200, 5, 3], 1), False)
        self.assertAlmostEqual(give_change([5, 10, 5, 50, 10, 20, 100, 200, 200, 5, 3], 5), True)
        self.assertAlmostEqual(give_change([5, 10, 5, 50, 10, 20, 100, 200, 200, 5, 3], 10), True)
        self.assertAlmostEqual(give_change([5, 10, 5, 50, 10, 20, 100, 200, 200, 5, 3], 15), True)
        self.assertAlmostEqual(give_change([5, 10, 5, 50, 10, 20, 100, 200, 200, 5, 3], 20), True)
        self.assertAlmostEqual(give_change([5, 10, 5, 50, 10, 20, 100, 200, 200, 5, 3], 24), False)
        #self.assertAlmostEqual(give_change([5, 10, 5, 50, 10, 20, 100, 200, 200, 5, 3], 25), True)
        #self.assertAlmostEqual(give_change([5, 10, 5, 50, 10, 20, 100, 200, 200, 5, 3], 30), True)
        #self.assertAlmostEqual(give_change([5, 10, 5, 50, 10, 20, 100, 200, 200, 5, 3], 35), True)
        #self.assertAlmostEqual(give_change([5, 10, 5, 50, 10, 20, 100, 200, 200, 5, 3], 40), True)
        #self.assertAlmostEqual(give_change([5, 10, 5, 50, 10, 20, 100, 200, 200, 5, 3], 45), True)
        self.assertAlmostEqual(give_change([5, 10, 5, 50, 10, 20, 100, 200, 200, 5, 3], 50), True)
        self.assertAlmostEqual(give_change([5, 10, 5, 50, 10, 20, 100, 200, 200, 5, 3], 59), False)
        #self.assertAlmostEqual(give_change([5, 10, 5, 50, 10, 20, 100, 200, 200, 5, 3], 95), True)
        #self.assertAlmostEqual(give_change([5, 10, 5, 50, 10, 20, 100, 200, 200, 5, 3], 98), True)
        #self.assertAlmostEqual(give_change([5, 10, 5, 50, 10, 20, 100, 200, 200, 5, 3], 103), True)
        #self.assertAlmostEqual(give_change([5, 10, 5, 50, 10, 20, 100, 200, 200, 5, 3], 608), True)
        self.assertAlmostEqual(give_change([5, 10, 5, 50, 10, 20, 100, 200, 200, 5, 3], 609), False)
        self.assertAlmostEqual(give_change([5, 10, 5, 50, 10, 20, 100, 200, 200, 5, 3], 1000), False)

        self.assertAlmostEqual(subtraction_from_change(10, {1:2, 2:2}, 2), 6)
        self.assertAlmostEqual(subtraction_from_change(100, {10: 100, 2: 2}, 2), 96)

        self.assertAlmostEqual(remove_coin_nominal([5, 1, 2, 3], 10), [5, 1, 2, 3])
        self.assertAlmostEqual(remove_coin_nominal([2, 10, 2, 30], 10), [2, 2, 30])