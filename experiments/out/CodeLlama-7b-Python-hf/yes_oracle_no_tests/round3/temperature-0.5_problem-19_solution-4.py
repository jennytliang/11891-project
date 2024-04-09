from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    return " ".join(sorted(numbers.split(), key=_))


def _(numbers: str) -> int:
    """
    >>> _('three one five')
    1
    >>> _('seven two five')
    2
    """
    return numbers.index(min(numbers.split()))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
