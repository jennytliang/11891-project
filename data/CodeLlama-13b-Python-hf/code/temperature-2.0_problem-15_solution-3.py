def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    if n == 0:
        return "0"
    else:
        return "0 " + string_sequence(n - 1) + str(n)


print(string_sequence(10))