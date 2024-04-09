from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    # split the string into a list of words
    words = numbers.split()

    # sort the words
    words.sort()

    # join the words into a single string
    return " ".join(words)


if __name__ == "__main__":
    # print("Example:")
    # print(sort_numbers("three one five"))

    # These "asserts" are used for self-checking and not for an auto-testing
    # assert sort_numbers("three one five") == "one three five"
    # assert sort_numbers("one two three") == "one two three"
    # assert sort_numbers("one two three five") == "one two three five"
    # assert sort_numbers("five three one") == "one three five"
    # assert sort_numbers("three five one") == "one three five"
    # print("Coding complete? Click 'Check' to earn cool rewards!")

    print(sort_numbers("three one five"))
