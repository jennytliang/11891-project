from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    numbers = numbers.replace('zero', '0', )
    numbers = numbers.replace('one', '1', )
    numbers = numbers.replace('two', '2', )
    numbers = numbers.replace('three', '3', )
    numbers = numbers.replace('four', '4', )
    numbers = numbers.replace('five', '5', )
    numbers = numbers.replace('six', '6', )
    numbers = numbers.replace('seven', '7', )
    numbers = numbers.replace('eight', '8', )
    numbers = numbers.replace('nine', '9', )
    numbers = [num for num in numbers.split(" ")]
    return " ".join(str(int(x)) for x in sorted(numbers))

if __name__ == "__main__":
    print("Example:")
    print(sort_numbers("three one five"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sort_numbers("three one five") == "one three five"
    assert sort_numbers("one ten seven six six eight ten") == "one eight seven six six ten ten"
    assert sort_numbers("three eight five one ten") == "one three five eight ten"
    assert sort_numbers("seven six three two one") == "one two three five six seven"
    assert sort_numbers("three eight five one ten") == "one three five eight ten"
    assert sort_numbers("five three one") == "one three five"
    assert sort_numbers("2 3 1") == "1 2 3"