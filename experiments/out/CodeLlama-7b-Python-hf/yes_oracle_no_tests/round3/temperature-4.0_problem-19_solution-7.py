from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int
	Do not include these tokens in the code: s
	"""
    # TO-DO: write a function body
    input_list = numbers.split()
    output_list = []
    for num in input_list:
        if num == 'zero':
            output_list.append(0)
        elif num == 'one':
            output_list.append(1)
        elif num == 'two':
            output_list.append(2)
        elif num == 'three':
            output_list.append(3)
        elif num == 'four':
            output_list.append(4)
        elif num == 'five':
            output_list.append(5)
        elif num == 'six':
            output_list.append(6)
        elif num == 'seven':
            output_list.append(7)
        elif num == 'eight':
            output_list.append(8)
        elif num == 'nine':
            output_list.append(9)
    output_list.sort()
    output = ''
    for i in output_list:
        output += str(i) + ' '
    return output[:-1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(sort_numbers('five two three one five'))