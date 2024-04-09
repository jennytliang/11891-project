from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""

    # get numbers
    nums = [num for num in numbers.split() if num.isdigit()]

    # convert to int
    nums_int = [int(num) for num in nums]

    # sort nums
    nums_int.sort()

    # convert to str
    nums_str = [str(num) for num in nums_int]

    # return string
    return ' '.join(nums_str)


if __name__ == "__main__":
    # Tests
    import doctest

    doctest.testmod()

    # Run
    print(sort_numbers("one four five three two"))
