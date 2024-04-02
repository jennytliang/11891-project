from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    
	Include these tokens in the code: min _ diff = float (" inf ")
	Do not include these tokens in the code: return
	"""

    numbers.sort(reverse=True)
    min_diff = float('inf')
    closest_numbers: List[float] = []
    for index in range(1, len(numbers)):
        diff = abs(numbers[index-1] - numbers[index])
        if diff < min_diff:
            min_diff = diff
            closest_numbers = [numbers[index-1], numbers[index]]
    return tuple(closest_numbers)
  
  
def find_largest_product(numbers: List[int]) -> float:
    """ From a supplied list of numbers (of length at least three), find three that when multiplied together produce
    the largest number and return them in order (largest, middle, smallest).
    >>> find_largest_product([1, 2, 3, 4, 1, 5])
    (5, 4, 3)
    >>> find_largest_product([1, 2, 3, 4, 1, 3])
    (6, 4, 3)
    >>> find_largest_product([5, 4, 3, 2, 1, 2])
    (12, 4, 3)
    """

    numbers.sort(reverse=True)
    if len(numbers) == 3:
        return tuple(numbers)
    if len(numbers) < 3:
        raise ValueError("Length of list should be at least 3.")
    largest_product = 1
    for index in range(len(numbers)-2):
        for j in range(index+1, len(numbers)-1):
            current_product = products = numbers[index] * numbers[j] * numbers[j+1]
            if current_product > largest_product:
                largest_product = current_product
                indices = [index, j, j+1]
                numbers_product = list(numbers)
    return tuple(numbers_product[indices[0]], numbers_product[indices[1]], numbers_product[indices[2]])


def find_closest_elements_with_min_and_max(numbers: List[float]) ->