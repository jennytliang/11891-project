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
        raise Exception('List must contain at least two numbers')

    number_of_numbers_minus_one = number_of_numbers - 1
    for index in range(0, number_of_numbers_minus_one):
        current_difference = abs(numbers[index] - numbers[index + 1])
        if index == 0:
            minimum_difference = current_difference
        else:
            previous_difference = abs(numbers[index - 1] - numbers[index])
            if current_difference < previous_difference:
                minimum_difference = current_difference
            else:
                minimum_difference = previous_difference

    minimum_difference_index = numbers.index(min(numbers))
    if minimum_difference_index == number_of_numbers_minus_one:
        index_of_smaller_number = minimum_difference_index - 1
        index_of_larger_number = minimum_difference_index
    elif minimum_difference_index == 0:
        index_of_smaller_number = minimum_difference_index
        index_of_larger_number = minimum_difference_index + 1
    else:
        index_of_smaller_number = minimum_difference_index - 1
        index_of_larger_number = minimum_difference_index + 1

    smaller_number = numbers[index_of_smaller_number]
    larger_number = numbers[index_of_larger_number]

    return smaller_number, larger_number


if __name__ == '__main__':
    import doctest

    doctest.testmod()
