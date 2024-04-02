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
        raise ValueError("The number list must contain at least two numbers")

    numbers.sort()
    first_number = numbers[0]
    last_number = numbers[number_of_numbers - 1]

    return first_number, last_number


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)

    # print("Please enter a list of at least two numbers:")
    # numbers = [float(x) for x in input().split()]
    # print(find_closest_elements(numbers))
