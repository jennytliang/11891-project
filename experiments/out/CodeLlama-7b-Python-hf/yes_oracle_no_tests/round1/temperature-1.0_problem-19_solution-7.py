from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""

    digit_count = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
                   "six": 6, "seven": 7, "eight": 8, "nine": 9}
    numbers = " ".join([num[0] for num in sorted(numbers.split(), key=lambda x: digit_count[x])])
    return numbers  # main solution function


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(sort_numbers("nine one five five six five"))
