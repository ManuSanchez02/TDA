import random

def random_sorted_array(n):
    return sorted(random.randint(0, 10000) for _ in range(n))
