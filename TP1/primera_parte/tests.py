import unittest
from utils import random_sorted_array
from kmerge_dyc import kmerge as kmerge_dyc
from kmerge_heap import kmerge as kmerge_heap


class TestKMergeDyC(unittest.TestCase):

    def setUp(self):
        self.array1 = random_sorted_array(10)
        self.array2 = random_sorted_array(10)
        return super().setUp()

    def test_merge_empty_array(self):
        self.assertEqual(
            kmerge_dyc([]), [], 'Merge of empty array returns empty array')

    def test_merge_empty_arrays(self):
        self.assertEqual(kmerge_dyc([], []), [],
                         'Merge of empty arrays returns empty array')

    def test_merge_one_array(self):
        self.assertEqual(kmerge_dyc(self.array1), self.array1,
                         'Merge of one arrays returns that array')

    def test_merge_two_arrays(self):
        self.assertEqual(kmerge_dyc(self.array1, self.array2), sorted(self.array1+self.array2),
                         'Merge of 2 arrays returns a merge of them')
    
    def test_merge_multiple_arrays(self):
        arrays = [random_sorted_array(10) for i in range(15)]
        expected = sorted([n for array in arrays for n in array])
        self.assertEqual(kmerge_dyc(*arrays), expected,
                         'Merge of 2 arrays returns a merge of them')
        
class TestKMergeHeaps(unittest.TestCase):

    def setUp(self):
        self.array1 = random_sorted_array(10)
        self.array2 = random_sorted_array(10)
        return super().setUp()

    def test_merge_empty_array(self):
        self.assertEqual(
            kmerge_heap([]), [], 'Merge of empty array returns empty array')

    def test_merge_empty_arrays(self):
        self.assertEqual(kmerge_heap([], []), [],
                         'Merge of empty arrays returns empty array')

    def test_merge_one_array(self):
        self.assertEqual(kmerge_heap(self.array1), self.array1,
                         'Merge of one arrays returns that array')

    def test_merge_two_arrays(self):
        self.assertEqual(kmerge_heap(self.array1, self.array2), sorted(self.array1+self.array2),
                         'Merge of 2 arrays returns a merge of them')
    
    def test_merge_multiple_arrays(self):
        arrays = [random_sorted_array(10) for i in range(15)]
        expected = sorted([n for array in arrays for n in array])
        self.assertEqual(kmerge_heap(*arrays), expected,
                         'Merge of 2 arrays returns a merge of them')


if __name__ == '__main__':
    unittest.main()
