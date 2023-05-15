import heapq
from utils import random_sorted_array

def initialize_heap(*arrays):
    heap = []
    for i in range(len(arrays)):
        if len(arrays[i]) > 0:
            heapq.heappush(heap, (arrays[i][0], i, 0))

    return heap

def push_next(heap, arrays, array_index, element_index):
    if element_index + 1 < len(arrays[array_index]):
        heapq.heappush(heap, (arrays[array_index][element_index + 1], array_index, element_index + 1))

def kmerge(*arrays):
    heap = initialize_heap(*arrays)

    res = []
    while len(heap) > 0:
        min_value, array_index, element_index = heapq.heappop(heap)
        push_next(heap, arrays, array_index, element_index)
        res.append(min_value)
    return res


if __name__ == '__main__':
    A = random_sorted_array(10)
    B = random_sorted_array(10)
    C = random_sorted_array(10)
    D = random_sorted_array(10)
    expected = sorted(A + B + C + D)
    assert kmerge(A, B, C, D) == expected
    print('OK')
