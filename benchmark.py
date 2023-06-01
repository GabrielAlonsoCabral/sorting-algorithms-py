from typing import List

from sorts.bubble_sort import bubble_sort
from sorts.insertion_sort import insertion_sort
from sorts.selection_sort import selection_sort
from utils import generate_random_array

randomic_array: List[list] = generate_random_array(10000, 0, 1000)


bubble_sort(randomic_array)
insertion_sort(randomic_array)
selection_sort(randomic_array)
