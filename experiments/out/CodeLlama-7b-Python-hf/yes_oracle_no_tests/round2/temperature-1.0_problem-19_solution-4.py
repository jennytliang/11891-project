from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    result = []
    arr_int = {'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'}
    numbers = numbers.split(" ")
    numbers.sort()
    for i in numbers:
        if i in arr_int:
            result.append(i)
        else:
            result.append(arr_int[i])
        return " ".join(result)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    
    import pytest

    pytest.main(["-v", "--doctest-modules", "--ignore=__init__.py", "."])