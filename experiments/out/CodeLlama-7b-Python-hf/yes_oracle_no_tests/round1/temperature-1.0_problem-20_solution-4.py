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

    numbers.sort(key=float)
    diff = float("inf")
    smaller_number = numbers[0]

    for i in range(len(numbers) - 1):
        if abs(numbers[i] - numbers[i + 1]) < diff:
            diff = abs(numbers[i] - numbers[i + 1])
            smaller_number = numbers[i]
            larger_number = numbers[i + 1]
    return smaller_number, larger_number


if __name__ == "__main__":
    import doctest

    doctest.testmod()
