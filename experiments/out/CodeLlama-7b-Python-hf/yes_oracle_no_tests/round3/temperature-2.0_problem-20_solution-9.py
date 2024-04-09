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


    number_of_numbers = len(numbers)
    if number_of_numbers < 2:
        raise ValueError("The list must contain at least two items")

    min_delta = float("inf")
    first_number = None
    second_number = None
    for i in range(number_of_numbers - 1):
        for j in range(i + 1, number_of_numbers):
            delta = abs(numbers[i] - numbers[j])
            if delta < min_delta:
                first_number = numbers[i]
                second_number = numbers[j]
                min_delta = delta

    return first_number, second_number


if __name__ == "__main__":
    import doctest

    doctest.testmod()
