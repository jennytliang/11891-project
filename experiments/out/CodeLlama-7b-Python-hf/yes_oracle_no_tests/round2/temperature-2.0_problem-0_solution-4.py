from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    
	Include these tokens in the code: sorted _ numbers
	"""
    numbers_sorted = sorted(numbers)
    for i in range(len(numbers_sorted) - 1):
        difference = numbers_sorted[i + 1] - numbers_sorted[i]
        if difference < threshold:
            return True
    return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
