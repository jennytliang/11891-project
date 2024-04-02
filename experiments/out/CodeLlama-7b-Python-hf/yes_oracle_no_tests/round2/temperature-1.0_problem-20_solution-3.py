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


    number_of_elements = len(numbers)

    if number_of_elements < 2:
        raise ValueError("List must contain at least two elements.")

    sorted_numbers = sorted(numbers)

    min_distance = float("inf")
    min_distance_first_element = float("inf")
    min_distance_second_element = float("inf")

    for i in range(number_of_elements - 1):
        distance = sorted_numbers[i + 1] - sorted_numbers[i]
        if distance < min_distance:
            min_distance = distance
            min_distance_first_element = sorted_numbers[i]
            min_distance_second_element = sorted_numbers[i + 1]

    return min_distance_first_element, min_distance_second_element


if __name__ == "__main__":
    import doctest

    doctest.testmod()
