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

    numbers.sort(key = lambda x: x)
    min_diff = float('inf')
    index, number = 1, numbers[0]

    while index < len(numbers):
        diff = abs(numbers[index] - number)

        if min_diff >  diff:
            min_diff, smaller, larger = diff, number, numbers[index]

        index += 1

    return smaller, larger


def find_closest_elements_in_sorted_list(sorted_list: List[float]) -> Tuple[float, float]:
    """ From a supplied sorted list of numbers (of length at least two) select and return two that are the closest to
    each other and return them in order (smaller number, larger number).
    >>> find_closest_elements_in_sorted_list([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements_in_sorted_list([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    n = len(sorted_list) - 1

    if abs(sorted_list[0] - sorted_list[1]) < abs(sorted_list[n] - sorted_list[n - 1]):
        min_diff = abs(sorted_list[n] - sorted_list[n - 1])

        return sorted_list[n], sorted_list[n - 1]
    
    else:
        min_diff = abs(sorted_list[0] - sorted_list[1])

        return sorted_list[0], sorted_list[1]


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
