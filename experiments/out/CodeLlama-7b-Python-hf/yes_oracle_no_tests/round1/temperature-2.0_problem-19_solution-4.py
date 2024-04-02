from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    # Split numbers into list
    num_list = numbers.split(" ")
    # Remove empty strings
    num_list = list(filter(lambda x: x != '', num_list))
    # Convert to ints
    num_list = list(map(lambda x: int(x), num_list))
    # Sort list
    num_list.sort()
    # Convert back to strings
    num_list = list(map(lambda x: str(x), num_list))
    # Return string of numbers
    return " ".join(num_list)


if __name__ == "__main__":
    print(sort_numbers("three one five"))
