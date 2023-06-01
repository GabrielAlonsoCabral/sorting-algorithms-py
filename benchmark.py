from sorts.bubble_sort import bubble_sort
from sorts.insertion_sort import insertion_sort
from sorts.merge_sort import merge_sort
from sorts.quick_sort import quick_sort
from sorts.selection_sort import selection_sort
from utils import generate_random_array

bubble_sort(generate_random_array(30000, 0, 1000))
insertion_sort(generate_random_array(30000, 0, 1000))
selection_sort(generate_random_array(30000, 0, 1000))
merge_sort(generate_random_array(30000, 0, 1000))
quick_sort(generate_random_array(30000, 0, 1000))
