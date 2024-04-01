from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    return any((numbers[i], numbers[i + 1]) < threshold for i in range(len(numbers) - 1))


def list_to_float(input_list: List[str]) -> List[float]:
    """ Returns given list casted as float.
    Raises an exception if some of strings could not be casted as float

    >>> list_to_float(['-3.0', '7.9'])
    [-3.0, 7.9]
    """
    result: List[float] = []
