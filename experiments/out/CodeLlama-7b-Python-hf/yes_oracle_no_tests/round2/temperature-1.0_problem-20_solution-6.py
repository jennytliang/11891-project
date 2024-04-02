from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    
	Include these tokens in the code: ()
	Do not include these tokens in the code: ( key = lambda x : x )
	"""


    number_1, number_2 = min(enumerate(numbers), key=lambda x: abs(x[1] - min(y for y in numbers if y > x[1])))
    return min(number_1, number_2), max(number_1, number_2)





if __name__ == '__main__':
    # input_numbers = [float(x) for x in input('type numbers separated by , ').split(',')]
    assert find_closest_elements([1.1, 3.2, 6.2, 6.5 ]) == (1.1, 3.2)
    import doctest

    doctest.testmod(verbose=True)