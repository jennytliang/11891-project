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


    number_of_numbers = len(numbers)
    if number_of_numbers < 2:
        raise Exception("The list must contain at least two numbers")

    # Find the smallest number and its index
    smallest_number, smallest_number_index = numbers[0], 0
    for i in range(1, number_of_numbers):
        if numbers[i] < smallest_number:
            smallest_number_index = i
            smallest_number = numbers[i]

    # Find the largest number and its index
    largest_number, largest_number_index = numbers[0], 0
    for i in range(1, number_of_numbers):
        if numbers[i] > largest_number:
            largest_number_index = i
            largest_number = numbers[i]

    # Return the smallest and largest numbers
    if smallest_number_index < largest_number_index:
        return numbers[smallest_number_index], numbers[largest_number_index]
    else:
        return numbers[largest_number_index], numbers[smallest_number_index]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
