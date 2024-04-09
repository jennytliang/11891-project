from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    numbers_list = numbers.split()
    numbers_list.sort(key=lambda x: int(x))
    return ' '.join(numbers_list)


if __name__ == "__main__":
    numbers = input("Enter a string of numbers: ")
    print(f'Smallest to largest: {sort_numbers(numbers)}')
