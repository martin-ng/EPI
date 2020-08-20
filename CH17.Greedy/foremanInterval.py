import unittest


class IntervalsTest(unittest.TestCase):

    def interval_one(self):
        result = foremanInterval(
            [[1, 2], [2, 3], [3, 4], [2, 3], [3, 4], [4, 5]])
        self.assertEqual(result, 2)


def foremanInterval(intervals):
    intervals.sort(key=lambda x: x[0])
    count, lastNum = 0, float('-inf')

    for interval in intervals:
        if interval[0] > lastNum:
            lastNum = interval[1]
            count += 1
    print(intervals)
    return count


if __name__ == '__main__':
    print(foremanInterval([[1, 2], [2, 3], [3, 4], [2, 3], [3, 4], [4, 5]]))
    unittest.main()
