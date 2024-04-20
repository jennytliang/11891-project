from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    
	Do not include these tokens in the code: number _ of _ numbers
	"""
    closest_elements = (numbers[0], numbers[1])
    for i in range(len(numbers) - 1):
        if abs(numbers[i] - numbers[i + 1]) < abs(closest_elements[0] - closest_elements[1]):
            closest_elements = (numbers[i], numbers[i + 1])
    return closest_elements


def find_closest_elements_one_liner(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements_one_liner([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements_one_liner([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    
	Do not include these tokens in the code: number _ of _ numbers
	"""
    return min(zip(numbers,numbers[1:]), key=lambda x: abs(x[0] - x[1]))


if __name__ == "__main__":
    import doctest
    doctest.testmod()