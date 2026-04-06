def deterministic_quicksort(arr):
    """Baseline quicksort with first-element pivot (intentionally vulnerable)."""
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return deterministic_quicksort(left) + [pivot] + deterministic_quicksort(right)
