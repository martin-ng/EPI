import unittest


class DeleteDupesTest(unittest.TestCase):

    def test_one(self):
        results = delete_duplicates([2, 3, 5, 5, 7, 11, 11, 11, 13])
        self.assertEquals(results, 6)


def delete_duplicates(arr):

    write = 1

    for read in range(1, len(arr)):
        if arr[write-1] != arr[read]:
            arr[write] = arr[read]
            write += 1

    return write


if __name__ == "__main__":
    unittest.main()
    print(delete_duplicates([2, 3, 5, 5, 7, 11, 11, 11, 13]))
