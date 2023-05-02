from utils import random_sorted_array


def merge(array1, array2):
    i = 0
    j = 0
    res = []
    while i < len(array1) and j < len(array2):
        if array1[i] > array2[j]:
            res.append(array2[j])
            j += 1
        else:
            res.append(array1[i])
            i += 1

    while i < len(array1):
        res.append(array1[i])
        i += 1

    while j < len(array2):
        res.append(array2[j])
        j += 1

    return res


def split(array):
    half = len(array) // 2
    return array[half:], array[:half]


def kmerge(*arrays):
    if len(arrays) == 1:
        return arrays[0]
    elif len(arrays) == 2:
        return merge(arrays[0], arrays[1])

    left_half, right_half = split(arrays)
    return merge(kmerge(*left_half), kmerge(*right_half))


if __name__ == '__main__':
    A = random_sorted_array(10)
    B = random_sorted_array(10)
    C = random_sorted_array(10)
    D = random_sorted_array(10)
    expected = sorted(A + B + C + D)
    assert kmerge(A, B, C, D) == expected
    print('OK')
