import random


def _insertion_sort_range(arr, lo, hi):
    for i in range(lo + 1, hi + 1):
        key = arr[i]
        j = i - 1
        while j >= lo and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def _three_way_partition(arr, lo, hi):
    pivot_index = random.randint(lo, hi)
    arr[lo], arr[pivot_index] = arr[pivot_index], arr[lo]
    pivot = arr[lo]

    lt = lo
    i = lo + 1
    gt = hi

    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1

    return lt, gt


def optimized_randomized_quicksort(arr, insertion_threshold=24):
    """
    Optimization technique: randomized pivot + three-way partition + small-partition insertion sort
    + tail recursion elimination via explicit stack.
    """
    if len(arr) <= 1:
        return arr

    stack = [(0, len(arr) - 1)]

    while stack:
        lo, hi = stack.pop()

        while lo < hi:
            if hi - lo + 1 <= insertion_threshold:
                _insertion_sort_range(arr, lo, hi)
                break

            lt, gt = _three_way_partition(arr, lo, hi)

            left_size = lt - lo
            right_size = hi - gt

            # Process smaller side first to keep stack shallow.
            if left_size < right_size:
                if gt + 1 < hi:
                    stack.append((gt + 1, hi))
                hi = lt - 1
            else:
                if lo < lt - 1:
                    stack.append((lo, lt - 1))
                lo = gt + 1

    return arr
