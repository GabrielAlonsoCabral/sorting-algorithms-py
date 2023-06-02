from typing import List

from decorators import log_execution_time


@log_execution_time
def selection_sort(arr: List[int]):
    n = len(arr)

    for i in range(n):
        min_index = i

        # Find the index of the minimum element in the unsorted part of the array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the minimum element with the current element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr
