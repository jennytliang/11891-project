from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    
	Include these tokens in the code: sorted _ numbers = sorted ( numbers )
	"""
    numbers = sorted(numbers)
    for i in range(len(numbers)):
        j = i + 1
        while j < len(numbers):
            if abs(numbers[i] - numbers[j]) < threshold:
                return True
            j += 1
    return False


def has_close_elements_two(numbers: List[float], threshold: float) -> bool:
    """ Another solution.
    """
    return any(abs(a - b) < threshold for a, b in zip(numbers, numbers[1:]))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
