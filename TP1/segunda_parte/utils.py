import random


def random_array(n):
    return [random.choice(range(1000)) for _ in range(n)]
