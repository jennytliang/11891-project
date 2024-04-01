from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    return " ".join(sorted(numbers.split()))


def sort_alphabetical(strings: str) -> str:
    """ Input is a space-delimited string of words.
    Return the string with words sorted alphabetically
    >>> sort_alphabetical('beta alpha gamma')
    'alpha beta gamma'
    """
    return " ".join(sorted(strings.split()))


def sort_case_insensitively(strings: str) -> str:
    """ Input is a space-delimited string of words.
    Return the string with words sorted case-insensitively
    >>> sort_case_insensitively('Beta Alpha Gamma')
    'alpha beta gamma'
    """
    return " ".join(sorted(strings.split(), key=lambda x: x.lower()))
