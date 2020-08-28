import unittest


class StringIntegerTest(unittest.TestCase):

    def test_one(self):
        results = integer_to_string(103)
        self.assertEqual(results, '103')

    def test_two(self):
        results = integer_to_string(100)
        self.assertEqual(results, '100')

    def test_three(self):
        results = integer_to_string(503)
        self.assertEqual(results, '503')


def integer_to_string(num):

    is_neg = False
    if num < 0:
        is_neg = True

    res = []

    while num != 0:
        n = num % 10
        res.append(chr(ord('0') + n))
        num //= 10

    return ('-' if is_neg else '') + (''.join(res[::-1]))


if __name__ == '__main__':
    unittest.main()
