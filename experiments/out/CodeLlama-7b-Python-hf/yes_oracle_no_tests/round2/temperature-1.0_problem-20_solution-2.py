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


    number_pairs = list(zip(numbers, numbers))
    sorted_with_necklaces = sorted(
        number_pairs,
        key=lambda x: abs(x[1] - x[0])
    )
    necklace_size = len(numbers)
    if necklace_size % 2 > 0:
        closest_two = sorted_with_necklaces[necklace_size // 2]
    else:
        second_number = sorted_with_necklaces[necklace_size // 2 - 1 : necklace_size // 2 + 1]
        closest_two = sorted(second_number, key=lambda x: x[0])[necklace_size // 2]
    return closest_two

if __name__ == "__main__":
    import doctest

    doctest.testmod()
