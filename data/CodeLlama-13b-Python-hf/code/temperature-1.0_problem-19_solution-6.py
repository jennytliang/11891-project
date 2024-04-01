from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    return " ".join(sorted(numbers.split()))


def sort_numbers_2(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from largest to smallest
    >>> sort_numbers_2('three one five')
    'five three one'
    """
    return " ".join(sorted(numbers.split(), reverse=True))


def sort_numbers_3(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted by last digit
    >>> sort_numbers_3('three one five')
    'one five three'
    """
    return " ".join(sorted(numbers.split(), key=lambda x: int(x[-1])))


def sort_numbers_4(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted by last digit, descending
    >>> sort_numbers_4('three one five')
    'five three one'
    """
    return " ".join(sorted(numbers.split(), key=lambda x: int(x[-1]), reverse=True))


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
