def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    return [element for element in l if element > 0 ]


def get_multiple(l: list, value: int):
    """
    Returns only the numbers that are multples of the given
    value. The original list must contain mostly positive numbers,
    including zero (but can also contain negative ones as well due to
    the given value not necessarily being positive, see the examples
    below. There will be no zero in the final result list, but other
    numbers that are actually zero are fine.

    Numbers that don't divide the value without a remainder are ok, we
    want the ones that return 1 in the division remainder, so those ones should
    be removed. The numbers can also be float, so we must use // not % - we can remove 
    the remainder, but that should only be done by calling the '//' operator, this
    works with int as well, but does return a float. We can not simply cast one side to
    an int, that will produce a float instead of the int (as this // operator is returning
    a float). If we simply cast both sides to int, it does not change the behaviour - as it will
    just do it in python 3, but it will do it in python 3 as well. The // is used to denote integer
    division, where / will do floating division.

    >>> get_multiple([-3, 1, 4, 8], 8)
    [4, 8]
    >>> get_multiple([-3, 1, 3, 6, 4, 8], 4)
    [3, 6, 8]
    """
