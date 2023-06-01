import random


def generate_random_array(size=0, min=1, max=100):
    # Generate a list of random integers between 1 and 100 (inclusive)
    arr = [random.randint(min, max) for _ in range(size)]
    return arr
