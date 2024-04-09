from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    
	Include these tokens in the code: ()
	Do not include these tokens in the code: ( reverse = True )
	"""


    number_pairs = []

    for i in range(0, len(numbers) - 1):
        number_pairs.append((abs(numbers[i] - numbers[i + 1]), numbers[i], numbers[i + 1]))

    number_pairs.sort(key=lambda x: x[0])

    return number_pairs[0][1:3]


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
