import random

def random_sorted_array(n, seed=None):
    random.seed(seed)
    return sorted(random.randint(0, 1000) for _ in range(n))
