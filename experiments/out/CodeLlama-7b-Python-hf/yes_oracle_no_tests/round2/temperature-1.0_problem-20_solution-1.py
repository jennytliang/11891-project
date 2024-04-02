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
        raise ValueError("numbers must contain at least two elements")

    # We start with the first two numbers in the list
    smallest_difference = abs(numbers[0] - numbers[1])
    closest_numbers = (numbers[0], numbers[1])

    for i in range(number_of_numbers - 1):
        for j in range(i + 1, number_of_numbers):
            difference = abs(numbers[i] - numbers[j])
            if difference < smallest_difference:
                smallest_difference = difference
                closest_numbers = (numbers[i], numbers[j])

    return closest_numbers


if __name__ == "__main__":
    import doctest

    doctest.testmod()
