import unittest


class PalindromeTest(unittest.TestCase):

    def test_one(self):
        results = is_palindrome('martin loves to code')
        self.assertEquals(results, False)

    def test_two(self):
        results = is_palindrome('aba')
        self.assertEquals(results, True)

    def test_three(self):
        results = is_palindrome('cbabc')
        self.assertEquals(results, True)


def is_palindrome(s):
    l = 0
    r = len(s) - 1
    while l < r:

        while l < r and not s[l].isalnum():
            l += 1

        while l < r and not s[r].isalnum():
            r -= 1

        if s[l].lower() != s[r].lower():
            return False

        l += 1
        r -= 1

    return True


if __name__ == "__main__":
    unittest.main()
