import unittest
'''
Naive Solution Time - O(2^N), Space - O(N)
Optimized      Time - O(N), Space - O(1)
'''


class TestFibonacci(unittest.TestCase):

    def test_fib_one(self):
        result = fibonacci(5)
        self.assertEqual(result, 5)
        result = fibonacci(6)
        self.assertEqual(result, 8)

    def test_fib_two(self):
        result = fibonacci_opt(5)
        self.assertEqual(result, 5)
        result = fibonacci(6)
        self.assertEqual(result, 8)


def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n-1) + fibonacci(n-2)


def fibonacci_opt(n):
    if n <= 1:
        return n

    first, second = 0, 1

    while n > 1:
        temp = second
        second = second + first
        first = temp
        n -= 1

    return second


if __name__ == '__main__':
    unittest.main()
