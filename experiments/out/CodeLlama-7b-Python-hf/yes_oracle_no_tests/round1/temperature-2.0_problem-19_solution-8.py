from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    tokens = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    numbers = numbers.split(" ")
    numbers = [tokens[x] for x in numbers]
    numbers.sort()
    numbers = [list(tokens.keys())[list(tokens.values()).index(x)] for x in numbers]
    return " ".join(numbers)


if __name__ == "__main__":
    print(sort_numbers("three one five"))
    print(sort_numbers("three one five two two"))
