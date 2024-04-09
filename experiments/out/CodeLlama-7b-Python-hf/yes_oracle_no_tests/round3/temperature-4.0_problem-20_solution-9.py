from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    
	Include these tokens in the code: ("
	Do not include these tokens in the code: ('
	"""



    numbers.sort()
    min_diff  = numbers[1] - numbers[0]
    min_diff_indexes = (0, 1)
    for i in range(len(numbers) - 1):
        if abs(numbers[i + 1] - numbers[i]) < min_diff:
            min_diff = numbers[i + 1] - numbers[i]
            min_diff_indexes = (i, i + 1)
    return numbers[min_diff_indexes[0]], numbers[min_diff_indexes[1]]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
