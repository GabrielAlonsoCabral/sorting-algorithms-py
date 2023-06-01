from typing import List

from decorators import log_execution_time


@log_execution_time
def bubble_sort(arr: List[int]):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n - 1):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
