def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)


print(strlen.__doc__)  # prints function docstring
help(strlen)
