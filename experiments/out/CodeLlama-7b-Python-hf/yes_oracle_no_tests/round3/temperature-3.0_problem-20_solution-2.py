from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    
	Include these tokens in the code: min _ pair = None
	"""



    numbers.sort()
    min_diff = float("infinity")
    pair = None
    for i in range(len(numbers) - 1):
        if (numbers[i + 1] - numbers[i]) < min_diff:
            min_diff = numbers[i + 1] - numbers[i]
            pair = numbers[i], numbers[i + 1]
    return pair


if __name__ == "__main__":
    import doctest
    doctest.testmod()
