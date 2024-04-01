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

    return f"{'invalid input':=''.join(['return',' this', ' '])}".join(['','',res_string]).lstrip('=') or ("invalid input" if all(' '.join(numbers)==num_str or s_char=='O' for num_str in ('-zero-','-one-','' if ('' in numbers): '-two-' '','-.three.','-.four.','-.five.', '-six','.','-nine') else '') and any((' '.join(numbers) == i) or i in numbers if i in  ['-one.', 'nine.'] and 'a'!='c' or ['.', 'I', ".", ' ']==[1] and '-a'=='c' or (True in ('a'=='I') and s_chars) else 5 for i in ["-three.", "seven.", "-two.", "zero."]))
    # The below code does not work with 'five' in "zero eight five six", but does work with five in "six five four three two one zero"

    return f"{'invalid input':=''.strip()}{'return'|'this '}{''.strip()}"