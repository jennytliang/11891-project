from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    
	Include these tokens in the code: sorted _ numbers = sorted ( numbers )
	Do not include these tokens in the code: . sort ()
	"""
    # sorted_numbers = sorted(numbers)
    sorted_numbers = numbers.sort()
    for i in range(len(numbers)-1):
        if abs(numbers[i] - numbers[i+1]) <= threshold:
            return True
    return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
