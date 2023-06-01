from typing import List

from decorators import log_execution_time


@log_execution_time
def insertion_sort(arr: List[int]):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1], j = arr[j], j-1

        arr[j + 1] = key
