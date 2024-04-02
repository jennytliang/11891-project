from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    out_str =  ' '.join([val for val in  sorted([[dict('zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'), int(i)][1] for i in numbers.split()])] )
    return out_str


# input = 'three one five'
# output = 'one three five'
# sort_numbers(input) == output
# input = 'five three one'
# output = 'one three five'
# sort_numbers(input) == output
# input = 'three three eight five five'
# output = 'three three five five eight'
# sort_numbers(input) == output
