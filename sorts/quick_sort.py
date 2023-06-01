from typing import List

from decorators import log_execution_time
from utils import generate_random_array


@log_execution_time
def quick_sort(arr: List[int]):
    quick_sort_no_execution_time(arr, 0, len(arr)-1)


def quick_sort_no_execution_time(arr: List[int], low: int, high: int):
    if low < high:
        pivot_index = choose_pivot(arr, low, high)
        # Move pivot to the end
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        pivot_index = partition(arr, low, high)
        quick_sort_no_execution_time(arr, low, pivot_index - 1)
        quick_sort_no_execution_time(arr, pivot_index + 1, high)


def choose_pivot(arr, low, high):
    mid = (low + high) // 2
    if arr[low] <= arr[mid] <= arr[high] or arr[high] <= arr[mid] <= arr[low]:
        return mid
    elif arr[mid] <= arr[low] <= arr[high] or arr[high] <= arr[low] <= arr[mid]:
        return low
    else:
        return high


def partition(arr, low, high):
    pivot = arr[high]  # Pivot is the last element
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
