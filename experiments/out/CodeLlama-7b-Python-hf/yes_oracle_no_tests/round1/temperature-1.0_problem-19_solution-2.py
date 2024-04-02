from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    pass


# tests
assert sort_numbers("three one five") == "one three five"
assert sort_numbers("zero one two three four five six seven eight nine") == "zero one two three four five six seven eight nine"
assert sort_numbers("nine eight seven six five four three two one zero") == "zero one two three four five six seven eight nine"
assert sort_numbers("five four three two one zero") == "zero one two three four five"
assert sort_numbers("five four three two one") == "one two three four five"
assert sort_numbers("one two three four five six seven eight nine") == "one two three four five six seven eight nine"
assert sort_numbers("nine eight seven six five four three two one") == "one two three four five six seven eight nine"
