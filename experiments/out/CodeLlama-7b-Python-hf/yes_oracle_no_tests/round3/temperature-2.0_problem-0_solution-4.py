from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    
	Include these tokens in the code: sorted
	Do not include these tokens in the code: numbers
	"""
    return any(
        abs(numbers[i] - numbers[i + 1]) < threshold for i in range(len(numbers) - 1)
    )


def has_close_elements_v2(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    
	Include these tokens in the code: sorted
	Do not include these tokens in the code: numbers
	"""
    return any(
        abs(numbers[i] - numbers[i + 1]) < threshold
        for i in range(len(numbers) - 1)
    )


def has_close_elements_v3(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    
	Include these tokens in the code: sorted
	Do not include these tokens in the code: numbers
	"""
    return any(
        abs(numbers[i] - numbers[i + 1]) < threshold
        for i in range(len(numbers) - 1)
    )
