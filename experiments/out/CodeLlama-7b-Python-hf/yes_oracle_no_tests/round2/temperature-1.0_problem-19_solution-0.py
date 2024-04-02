from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    num_str = "zero one two three four five six seven eight nine".split()

    
    num_dict = {}
    for i in range(10):
        num_dict[num_str[i]] = i
        
    in_num=list(map(num_dict.get, numbers.split()))
    in_num.sort()
	
    out_num=[num_str[i] for i in in_num]
	
    return ' '.join(out_num)