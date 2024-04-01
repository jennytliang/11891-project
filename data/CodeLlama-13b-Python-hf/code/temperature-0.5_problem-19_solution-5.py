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
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers_2('three one five')
    'one three five'
    """
    return " ".join(sorted(numbers.split(), key=lambda x: int(x)))


def sort_numbers_3(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers_3('three one five')
    'one three five'
    """
    return " ".join(sorted(numbers.split(), key=lambda x: int(x[0])))


def sort_numbers_4(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers_4('three one five')
    'one three five'
    """
    return " ".join(sorted(numbers.split(), key=lambda x: int(x[0])))


def sort_numbers_5(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers_5('three one five')
    'one three five'
    """
    return " ".join(sorted(numbers.split(), key=lambda x: int(x[0])))


def sort_numbers_6(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers_6('three one five')
    'one three five'
    """
    return " ".join(sorted(numbers.split(), key=lambda x: int(x[0])))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
