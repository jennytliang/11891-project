from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code:   to _ int = {' zero
	"""

    tokens_to_int = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    num_list = numbers.split(" ")
    num_list = [tokens_to_int[num] for num in num_list]
    num_list.sort()
    num_list = [str(num) for num in num_list]
    return " ".join(num_list)


if __name__ == "__main__":
    print(sort_numbers("three one five"))
