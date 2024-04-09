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


    number_to_index_mapping = {number: index for index, number in enumerate(numbers)}
    closest_pair = min(
        (abs(numbers[index] - numbers[index + 1]), (numbers[index], numbers[index + 1]))
        for index in range(len(numbers) - 1)
    )

    return closest_pair[1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
