from main import *
import unittest


class TestChange(unittest.TestCase):
    coins = [5, 10, 5, 50, 10, 20, 100, 200, 200, 5, 3]

    def test_give_change_with_one_coin(self):
        self.assertAlmostEqual(give_change(TestChange.coins, 5), True)
        self.assertAlmostEqual(give_change(TestChange.coins, 10), True)
        self.assertAlmostEqual(give_change(TestChange.coins, 20), True)

    @unittest.skip("The code is being finalized for these tests.")
    def test_give_change_with_few_coins(self):
        self.assertAlmostEqual(give_change(TestChange.coins, 15), True)
        self.assertAlmostEqual(give_change(TestChange.coins, 25), True)
        self.assertAlmostEqual(give_change(TestChange.coins, 30), True)

    def test_cant_give_change_for_small_coin(self):
        self.assertAlmostEqual(give_change(TestChange.coins, 1), False)
        self.assertAlmostEqual(give_change(TestChange.coins, 2), False)

    def test_cant_give_change_with_few_coins(self):
        self.assertAlmostEqual(give_change(TestChange.coins, 24), False)
        self.assertAlmostEqual(give_change(TestChange.coins, 59), False)
        self.assertAlmostEqual(give_change(TestChange.coins, 609), False)

    def test_subtraction_coins_from_change(self):
        self.assertAlmostEqual(subtraction_from_change(10, {1: 2, 2: 2}, 2), 6)
        self.assertAlmostEqual(subtraction_from_change(100, {10: 100, 2: 2}, 2), 96)

    def test_remove_coin_nominal_from_coins(self):
        self.assertAlmostEqual(remove_coin_nominal([5, 1, 2, 3], 10), [5, 1, 2, 3])
        self.assertAlmostEqual(remove_coin_nominal([2, 10, 2, 30], 10), [2, 2, 30])


if __name__ == '__main__':
    unittest.main()
