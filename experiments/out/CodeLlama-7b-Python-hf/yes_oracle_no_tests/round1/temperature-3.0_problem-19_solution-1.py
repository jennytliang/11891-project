from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""

    # TODO: write your code here
    # remove all spaces
    numbers = numbers.replace(" ", "")

    # split into a list of numbers
    numbers = numbers.split()

    # get the minimum number
    min_number = min(numbers)

    # get the maximum number
    max_number = max(numbers)

    # get the middle number
    middle_number = numbers[len(numbers) // 2]

    # create a list with the minimum, middle, and maximum numbers
    list_of_numbers = [min_number, middle_number, max_number]

    # sort the list
    list_of_numbers.sort()

    # get the string of the list
    sorted_numbers = " ".join(list_of_numbers)

    return sorted_numbers


def sort_numbers_2(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""

    # TODO: write your code here
    # remove all spaces
    numbers = numbers.replace(" ", "")

    # split into a list of numbers
    numbers = numbers.split()

    # get the minimum number
    min_number = min(numbers)

    # get the maximum number
    max_number = max(numbers)

    # get the middle number
    middle_number = numbers[len(numbers) // 2]

    # create a list with the minimum, middle, and maximum numbers
    list_of_numbers = [min_number, middle_number, max_number]

    # sort the list
    list_of_numbers.sort()

    # get the string of the list
    sorted_numbers = " ".join