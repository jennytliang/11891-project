from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    # valid_nums = sorted(list(map(str, list(range(0, 10))))) # or valid_nums = ['zero'] through 'nine'
    valid_nums = list(range(10))
    numlist = []

    for number in numbers.split(" "):
        numlist += next((i for i in valid_nums if i==number.replace('zero','') and i[1:]) or [number])

    sorted_numlist, i = (list(reversed(numlist)),0) if (numlist!=valid_nums) else (numlist,[])
    while i < len(sorted_numlist):
        sorted_numlist[i] = 0 if sorted_numlist[i] is numlist[-1] else 'zero'
        i += 1
    
    res_string = " ".join([str(val) for val in sorted(numlist[-1::-1])]).lstrip()

    return f"{'invalid input':=''.join(['return',' this', ' '])}".join(['','',res_string]).lstrip('= ')