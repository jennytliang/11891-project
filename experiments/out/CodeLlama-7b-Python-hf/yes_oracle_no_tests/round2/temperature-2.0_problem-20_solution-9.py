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
    min_diff = float(" inf ")
    for i in range(len(numbers) - 1):
        if abs(numbers[i + 1] - numbers[i]) < min_diff:
            min_diff = abs(numbers[i + 1] - numbers[i])
            result = (numbers[i], numbers[i + 1])
    return result


def find_closest_elements_2(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements_2([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements_2([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    
	Include these tokens in the code: min _ diff = float (" inf ")
	Do not include these tokens in the code: return
	"""

    numbers.sort(reverse=True)
    min_diff = float(" inf ")
    for i in range(len(numbers) - 1):
        if abs(numbers[i + 1] - numbers[i]) < min_diff:
            diff = numbers[i + 1] - numbers[i]
            result = (numbers[i + 1], numbers[i])
    return result


def find_closest_elements_3(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements_3([1.0, 2.0, 3.0, 4.0, 5.0,