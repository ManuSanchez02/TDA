from utils import random_sorted_array
from math import inf
import heapq

# Details
# heapq.heappush complexity: O(log(n))
# heapq.heappop complexity: O(log(n))

class HeapElement:
    def __init__(self, arrays, array_index, element_index):
        self.value = arrays[array_index][element_index]
        self.array_index = array_index
        self.element_index = element_index

    def __lt__(self, other):
        return self.value < other

    def __gt__(self, other):
        return self.value > other

# O(k)
def initialize_heap(*arrays):
    heap = []

    # O(k)
    for i, array in enumerate(arrays):
        if len(array) > 0:
            element = HeapElement(arrays, i, 0)
            heap.append(element)

    # O(k)
    heapq.heapify(heap)
    return heap

# O(log(k))
def push_next(heap, arrays, array_index, element_index):
    if element_index + 1 < len(arrays[array_index]):
        new_element = HeapElement(arrays, array_index, element_index + 1)
        heapq.heappush(heap, new_element)
    else:
        heapq.heappush(heap, inf)

# O(k) + O(k*h*log(k)) = O(k*h*log(k))
# O(N*log(k))
def kmerge(*arrays):
    # O(k)
    heap = initialize_heap(*arrays)
    
    res = []

    # O (k*h)
    while len(res) < len(arrays) * len(arrays[0]):

        # O(log k)
        min_value = heapq.heappop(heap)

        # O(log k)
        push_next(heap, arrays, min_value.array_index, min_value.element_index)
        res += [min_value.value]
    return res


if __name__ == '__main__':
    A = random_sorted_array(10)
    B = random_sorted_array(10)
    C = random_sorted_array(10)
    D = random_sorted_array(10)
    expected = sorted(A + B + C + D)
    assert kmerge(A, B, C, D) == expected
    print('OK')
