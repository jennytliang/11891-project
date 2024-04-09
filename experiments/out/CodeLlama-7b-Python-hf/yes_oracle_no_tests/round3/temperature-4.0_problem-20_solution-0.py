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


    number_of_elements = len(numbers)
    if number_of_elements < 2:
        raise Exception("There are too few elements in the list")

    closest_distance = float("inf")
    first_element = None
    second_element = None
    for i in range(0, number_of_elements - 1):
        for j in range(i + 1, number_of_elements):
            distance = abs(numbers[i] - numbers[j])
            if distance < closest_distance:
                first_element = numbers[i]
                second_element = numbers[j]
                closest_distance = distance
    return first_element, second_element


if __name__ == '__main__':
    import doctest

    doctest.testmod()
