import unittest


class SubsequenceTest(unittest.TestCase):

    def subsequence_one(self):
        result = increasingSubsequence([1, 2, 3, 4, 5])
        self.assertEqual(result, 7)

    def subsequence_two(self):
        result = increasingSubsequence([5, 4, 3, 2, 1])
        self.assertEqual(result, 0)


def increasingSubsequence(arr):
    dp = [0 for _ in range(len(arr))]


if __name__ == "__main__":
    unittest.main()
