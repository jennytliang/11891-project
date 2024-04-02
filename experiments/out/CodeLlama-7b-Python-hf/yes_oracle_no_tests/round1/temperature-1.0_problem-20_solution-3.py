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

    numbers.sort(key=lambda x: abs(x))
    min_diff = float("inf")
    closest_numbers = []
    for i, number in enumerate(numbers):
        if i < len(numbers) - 1:
            diff = abs(numbers[i] - numbers[i + 1])
            if diff < min_diff:
                closest_numbers = [numbers[i], numbers[i + 1]]
                min_diff = diff
    return tuple(closest_numbers)


def find_closest_elements_v2(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements_v2([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements_v2([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    
	Include these tokens in the code: min _ diff = float (" inf ")
	Do not include these tokens in the code: return
	"""

    numbers.sort(key=lambda x: abs(x))
    min_diff = float("inf")
    closest_numbers = []
    for i, number in enumerate(numbers):
        if i < len(numbers) - 1:
            diff = abs(numbers[i] - numbers[i + 1])
            if diff < min_diff:
                closest_numbers = [numbers[i], numbers[i + 1]]
                min_diff = diff
    return tuple(closest_numbers)


def find_closest_elements_v3(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
   