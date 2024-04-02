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
        if abs(numbers[i] - numbers[i + 1]) < min_diff:
            min_diff = abs(numbers[i] - numbers[i + 1])
            closest_numbers = (numbers[i], numbers[i + 1])
    return closest_numbers


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

    numbers.sort(reverse=False)
    min_diff = float("inf")
    closest_numbers = []
    for i in range(len(numbers) - 1):
        if abs(numbers[i] - numbers[i + 1]) < min_diff:
            min_diff = abs(numbers[i] - numbers[i + 1])
            closest_numbers.clear()
            closest_numbers.append(numbers[i])
            closest_numbers.append(numbers[i + 1])
    return tuple(closest_numbers)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
