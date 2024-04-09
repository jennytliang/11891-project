from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    
	Include these tokens in the code: ()
	Do not include these tokens in the code: ( key = lambda x : abs ( x ))
	"""


    number_pairs = []
    for number in numbers:
        for other_number in numbers:
            if number != other_number:
                number_pairs.append((number, other_number))

    return min(number_pairs, key=lambda x: abs(x[0] - x[1]))


if __name__ == '__main__':
    import doctest

    doctest.testmod()
