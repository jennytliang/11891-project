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

    numbers.sort(reverse=False)
    min_diff = float("inf")
    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if diff < min_diff:
            min_diff = diff
            min_diff_indices = (numbers[i], numbers[i + 1])
    return min_diff_indices


def find_smallest_difference(numbers_a: List[float], numbers_b: List[float]) -> Tuple[float, float]:
    """ From two supplied lists of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_smallest_difference([1.0, 2.0, 3.0, 4.0, 5.0], [10.0, 4.0, 1.0, 9.0, 3.0])
    (1.0, 3.0)
    >>> find_smallest_difference([1.0, 2.0, 3.0, 4.0, 5.0], [10.0, 4.0, 1.0, 9.0, 3.0, 2.0])
    (1.0, 3.0)
    
	Include these tokens in the code: min _ diff = float (" inf ")
	Do not include these tokens in the code: return
	"""

    numbers_a.sort(reverse=False)
    numbers_b.sort(reverse=False)
    min_diff = float("inf")
    for i in range(len(numbers_a) - 1):
        for j in range(len(numbers_b) - 1):
            diff = abs(numbers_a[i] - numbers_b[j])
            if diff < min_diff:
                min_diff = diff
                min_diff_indices = (numbers_a[i], numbers_b[j])
    return min_diff_indices
