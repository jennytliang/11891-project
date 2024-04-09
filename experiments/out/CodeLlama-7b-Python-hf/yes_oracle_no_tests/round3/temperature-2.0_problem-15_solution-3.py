def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    
	Do not include these tokens in the code: def string _ sequence _ 2 ( n :
	"""

    return " ".join(map(str, range(n + 1)))


def main():
    """
    Usage:
        python string_sequence.py
        python string_sequence.py 5
        python string_sequence.py 10
    """
    import doctest
    doctest.testmod()
    # n = int(input())
    # print(string_sequence(n))


if __name__ == '__main__':
    main()