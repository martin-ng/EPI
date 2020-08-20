import unittest


class CoinTest(unittest.TestCase):

    def change_making_one(self):
        results = change_making(58)
        self.assertEqual(results, 5)

    def change_making_two(self):
        results = change_making(100)
        self.assertEqual(results, 1)

    def change_making_two(self):
        results = change_making(75)
        self.assertEqual(results, 3)


def change_making(coin):
    COINS = [100, 50, 25, 10, 5, 1]
    num_coins = 0

    for c in COINS:
        num_coins += coin // c
        coin = coin % c
    return num_coins


if __name__ == "__main__":
    unittest.main()
