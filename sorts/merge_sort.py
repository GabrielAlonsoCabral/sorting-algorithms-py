from typing import List

from decorators import log_execution_time


@log_execution_time
def merge_sort(arr: List[int]):
    merge_sort_without_log(arr=arr)


def merge_sort_without_log(arr):
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursive calls to sort the two halves
    left_half = merge_sort_without_log(left_half)
    right_half = merge_sort_without_log(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = right_index = 0

    # Merge the two sorted halves into a single sorted array
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Append any remaining elements from the left or right halves
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged
