from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    return " ".join(sorted(numbers.split()))


def sort_numbers_list(numbers: List[str]) -> List[str]:
    """ Input is a list of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the list with numbers sorted from smallest to largest
    >>> sort_numbers_list(['three', 'one', 'five'])
    ['one', 'three', 'five']
    """
    return sorted(numbers)