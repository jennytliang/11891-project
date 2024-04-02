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
    for i in range(len(sorted_numbers) - 1):
        difference = abs(sorted_numbers[i] - sorted_numbers[i + 1])
        if difference < threshold:
            return True
    return False


def get_average_distance(numbers: List[float]) -> float:
    """ Calculate average distance between consecutive numbers in given list.
    >>> get_average_distance([1.0, 2.0, 3.0])
    1.0
    >>> get_average_distance([1.0, 2.8, 3.0, 4.0, 5.0, 2.0])
    0.54
    """
    sorted_numbers = sorted(numbers)
    average_distance = 0
    for i in range(len(sorted_numbers) - 1):
        average_distance += abs(sorted_numbers[i] - sorted_numbers[i + 1])
    return average_distance / (len(sorted_numbers) - 1)


def get_average_distance_to_neighbours(numbers: List[float]) -> float:
    """ Calculate average distance between a number and its two neighbours.
    >>> get_average_distance_to_neighbours([1.0, 2.0, 3.0])
    1.0
    >>> get_average_distance_to_neighbours([1.0, 2.8, 3.0, 4.0, 5.0, 2.0])
    0.8
    """
    sorted_numbers = sorted(numbers)
    average_distance = 0
    for i in range(len(sorted_numbers) - 2):
        average_distance += abs(sorted_numbers[i] - sorted_numbers[i + 2])
    return average_distance / (len(sorted_numbers) - 2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
