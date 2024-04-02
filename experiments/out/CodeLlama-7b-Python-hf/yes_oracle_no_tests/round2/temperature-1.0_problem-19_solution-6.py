from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    digit = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    digit_keys= digit.keys()
    if numbers:
        s = ''.join(digit[x] for x in numbers.split())
    s = int(s)
    return str(s)


if __name__ == "__main__":
    # Test
    assert sort_numbers("three one five") == "one three five"
    assert sort_numbers("two two two") == "two two two"
    assert sort_numbers("two two five four three four five four three six six eight seven six") == "three four four five five four four four four six six six seven eight"
    assert sort_numbers("one eight") == "eight one"
