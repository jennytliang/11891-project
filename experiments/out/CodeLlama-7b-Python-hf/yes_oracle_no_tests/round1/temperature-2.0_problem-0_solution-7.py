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
    sorted_numbers = sorted(numbers)
    for i in range(len(sorted_numbers)):
        for j in range(i + 1, len(sorted_numbers)):
            if abs(sorted_numbers[i] - sorted_numbers[j]) <= threshold:
                return True
    return False


def has_close_elements_linear(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements_linear([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements_linear([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    
	Include these tokens in the code: for _ i in range _ numbers: for _ j in range _ numbers:
	"""
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) <= threshold:
                return True
    return False


def has_close_elements_binary(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements_binary([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements_binary([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    
	Include these tokens in the code: for _ i in range _ len _ numbers: for _ j in range _ len _ numbers:
	"""
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) <= threshold:
                return True
    return