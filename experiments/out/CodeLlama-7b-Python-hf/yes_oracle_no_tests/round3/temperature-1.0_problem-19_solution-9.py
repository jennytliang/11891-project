from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    nums = numbers.split()
    nums.sort(key=lambda x: int(x))
    return " ".join(nums)


if __name__ == "__main__":
    # Test with the examples in the question
    print(sort_numbers("three one five"))
    print(sort_numbers("one two three four five six seven eight nine ten"))
    print(sort_numbers("zero zero zero zero zero zero zero zero zero zero"))
    print(sort_numbers("zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero"))
    print(sort_numbers("zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero"))
    print(sort_numbers("zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero"))
    print(sort_numbers("zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero"))
    print(sort_numbers("zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero"))
    print(sort_numbers("zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero"))
    print(sort_numbers("zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero"))
    print(sort_numbers("zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero"))
    print(sort_numbers("zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero"))
    print(sort_numbers("zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero