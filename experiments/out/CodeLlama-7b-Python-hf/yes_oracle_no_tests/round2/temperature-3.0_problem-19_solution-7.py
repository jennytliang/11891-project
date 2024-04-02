from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    tokens = numbers.split()
    numbers_list = []
    for token in tokens:
        if token in int:
            numbers_list.append(int[token])
    sorted_numbers = sorted(numbers_list)
    sorted_tokens = []
    for number in sorted_numbers:
        for key, value in int.items():
            if value == number:
                sorted_tokens.append(key)
    return ' '.join(sorted_tokens)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
