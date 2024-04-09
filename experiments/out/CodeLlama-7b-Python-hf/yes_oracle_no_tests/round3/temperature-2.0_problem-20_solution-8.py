from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    
	Include these tokens in the code: ()
	Do not include these tokens in the code: ( reverse = False )
	"""


    number_difference = numbers[0] - numbers[1]
    number_1 = numbers[0]
    number_2 = numbers[1]
    for i in range(2, len(numbers)):
        if abs(numbers[i] - numbers[i - 1]) < number_difference:
            number_difference = abs(numbers[i] - numbers[i - 1])
            number_1 = numbers[i - 1]
            number_2 = numbers[i]
        elif abs(numbers[i] - numbers[i - 1]) == number_difference:
            if numbers[i] < number_1:
                number_1 = numbers[i - 1]
                number_2 = numbers[i]
            elif numbers[i] > number_2:
                number_1 = numbers[i - 1]
                number_2 = numbers[i]
    return number_1, number_2


if __name__ == "__main__":
    import doctest

    doctest.testmod()
