from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    
	Do not include these tokens in the code: number _ list = []
	"""
    if len(numbers) < 2:
        raise ValueError("No numbers to compare.")

    selected_numbers = numbers[0:2]
    smallest_difference = abs(selected_numbers[0] - selected_numbers[1])

    for index in range(2, len(numbers)):
        difference = abs(numbers[index] - selected_numbers[0])
        if difference < smallest_difference:
            smallest_difference = difference
            selected_numbers[1] = numbers[index]
        else:
            difference = abs(numbers[index] - selected_numbers[1])
            if difference < smallest_difference:
                smallest_difference = difference
                selected_numbers[0] = numbers[index]

    return tuple(selected_numbers)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
