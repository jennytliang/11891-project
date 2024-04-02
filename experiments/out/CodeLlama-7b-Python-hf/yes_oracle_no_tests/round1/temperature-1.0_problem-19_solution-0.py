from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    return ' '.join(sorted(numbers.split(), key=lambda x: _[x]))


if __name__ == "__main__":
    # Test your code with this first
    # Change the expected output and run to test your code
    print("Testing...")
    assert sort_numbers("five three one") == "one three five", "Three 1"
    assert sort_numbers("five three two one") == "one three two five", "Three 2"
    assert sort_numbers("five three two one nine nine nine nine") == "one nine nine nine three two five", "Three 3"
    assert sort_numbers("five three two one nine nine nine nine zero") == "zero nine nine nine three two five", "Three 4"
    assert sort_numbers("five three two one nine nine nine nine zero zero") == "zero zero nine nine nine three two five", "Three 5"
    assert sort_numbers("five three two one nine nine nine nine zero zero zero") == "zero zero zero nine nine nine three two five", "Three 6"
    assert sort_numbers("five three two one nine nine nine nine zero zero zero zero") == "zero zero zero zero nine nine three two five", "Three 7"
    assert sort_numbers("five three two one nine nine nine nine zero zero zero zero zero") == "zero zero zero zero zero nine nine three two five", "Three 8"
    assert sort_numbers("five three two one nine nine nine nine zero zero zero zero zero zero") == "zero zero zero zero zero zero nine nine three two five", "Three 9"
    
    print("Coding complete? Click 'Check' to earn cool rewards!")
