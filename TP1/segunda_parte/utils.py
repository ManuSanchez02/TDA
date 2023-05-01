import random


def random_array(n):
    return [random.randint(0, 1000) for _ in range(n)]
