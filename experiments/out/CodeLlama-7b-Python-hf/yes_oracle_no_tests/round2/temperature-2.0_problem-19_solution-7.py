from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    numbers = numbers.replace('zero', '0')
    numbers = numbers.replace('one', '1')
    numbers = numbers.replace('two', '2')
    numbers = numbers.replace('three', '3')
    numbers = numbers.replace('four', '4')
    numbers = numbers.replace('five', '5')
    numbers = numbers.replace('six', '6')
    numbers = numbers.replace('seven', '7')
    numbers = numbers.replace('eight', '8')
    numbers = numbers.replace('nine', '9')
    numbers = numbers.replace(' ', '')
    numbers = numbers.split('')
    numbers.sort()
    numbers = ''.join(numbers)
    return numbers


if __name__ == '__main__':
    import doctest

    doctest.testmod()
