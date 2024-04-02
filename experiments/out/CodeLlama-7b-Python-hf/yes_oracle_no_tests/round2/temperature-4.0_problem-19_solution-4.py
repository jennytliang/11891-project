from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    # split the string into a list
    lst = numbers.split()
    # convert the list into a list of ints
    int_lst = [int(i) for i in lst]
    # sort the list
    int_lst.sort()
    # convert the list back into a string
    result = ' '.join(map(str, int_lst))
    return result


if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    print(sort_numbers('three one five'))
    print(sort_numbers('three one five seven four nine two three'))
