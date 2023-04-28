import unittest
from utils import random_sorted_array

# -------------------------------
# |    COMMENT ONE OF THESE:    |
# -------------------------------
# from kmerge_dyc import kmerge
from kmerge_heap import kmerge


class TestKMerge(unittest.TestCase):

    def setUp(self):
        self.array1 = random_sorted_array(10)
        self.array2 = random_sorted_array(10)
        return super().setUp()

    def test_merge_empty_array(self):
        self.assertEqual(
            kmerge([]), [], 'Merge of empty array returns empty array')

    def test_merge_empty_arrays(self):
        self.assertEqual(kmerge([], []), [],
                         'Merge of empty arrays returns empty array')

    def test_merge_one_array(self):
        self.assertEqual(kmerge(self.array1), self.array1,
                         'Merge of one arrays returns that array')

    def test_merge_two_arrays(self):
        self.assertEqual(kmerge(self.array1, self.array2), sorted(self.array1+self.array2),
                         'Merge of 2 arrays returns a merge of them')
    
    def test_merge_multiple_arrays(self):
        arrays = [random_sorted_array(10) for i in range(15)]
        expected = sorted([n for array in arrays for n in array])
        self.assertEqual(kmerge(*arrays), expected,
                         'Merge of 2 arrays returns a merge of them')


if __name__ == '__main__':
    unittest.main()
