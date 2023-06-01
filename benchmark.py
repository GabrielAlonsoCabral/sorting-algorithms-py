from sorts.bubble_sort import bubble_sort
from sorts.insertion_sort import insertion_sort
from sorts.merge_sort import merge_sort
from sorts.quick_sort import quick_sort
from sorts.selection_sort import selection_sort
from utils import generate_random_array

ARRAY_SIZE = 30000
MIN_VALUE = 0
MAX_VALUE = 1000

bubble_sort(generate_random_array(ARRAY_SIZE, MIN_VALUE, MAX_VALUE))
insertion_sort(generate_random_array(ARRAY_SIZE, MIN_VALUE, MAX_VALUE))
selection_sort(generate_random_array(ARRAY_SIZE, MIN_VALUE, MAX_VALUE))
merge_sort(generate_random_array(ARRAY_SIZE, MIN_VALUE, MAX_VALUE))
quick_sort(generate_random_array(ARRAY_SIZE, MIN_VALUE, MAX_VALUE))
