from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    # split() returns a list of the string, separated at each whitespace
    # map() returns the item in the list being iterated over,
    # as the function supplied to map() is applied to it
    # sort() sorts a list in ascending order
    # join() returns a string with items separated by a specified string (space in this case)
    # return statement joins the sorted string list by spaces
    return ' '.join(sorted(map(lambda x: x.lower(),
                               numbers.split(' '))))

