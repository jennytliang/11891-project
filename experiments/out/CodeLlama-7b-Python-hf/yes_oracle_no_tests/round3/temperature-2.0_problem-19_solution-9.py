from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    # numbers = 'seven four one four three five five five'
    # numbers = 'zero zero one zero zero two three three'
    # numbers = 'seven four one four three five five five'
    numbers = 'zero zero one zero zero two three three'
    # numbers = 'zero zero one zero zero two three'
    
    str_list = numbers.split(' ')
    num_list = []
    for num in str_list:
        num_list.append(int(num))
    num_list.sort()
    new_str = ''
    for num in num_list:
        new_str += str(num) + ' '
    return new_str.strip()


if __name__ == '__main__':
    print(sort_numbers('three one five'))
    print(sort_numbers('zero zero one zero zero two three three'))
