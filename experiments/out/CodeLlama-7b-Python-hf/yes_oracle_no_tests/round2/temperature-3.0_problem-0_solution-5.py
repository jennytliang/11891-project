from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    
	Include these tokens in the code: i
	Do not include these tokens in the code: index , number
	"""

    sorted_numbers = sorted(numbers)
  
    for i in range(len(sorted_numbers)-1):
        if abs(sorted_numbers[i]-sorted_numbers[i+1]) < threshold:
            return True
    return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
