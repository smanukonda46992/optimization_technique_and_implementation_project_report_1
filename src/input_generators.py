import random


def random_array(size, low=0, high=10**6):
    return [random.randint(low, high) for _ in range(size)]


def sorted_array(size):
    return list(range(size))


def reverse_sorted_array(size):
    return list(range(size, 0, -1))


def nearly_sorted_array(size, swaps_ratio=0.02):
    arr = list(range(size))
    swaps = max(1, int(size * swaps_ratio))
    for _ in range(swaps):
        i = random.randint(0, size - 1)
        j = random.randint(0, size - 1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr


def duplicate_heavy_array(size, unique_ratio=0.1):
    unique_count = max(2, int(size * unique_ratio))
    pool = [random.randint(0, 10000) for _ in range(unique_count)]
    return [random.choice(pool) for _ in range(size)]
