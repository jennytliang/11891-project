def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    length = 0
    for _ in string:
        length += 1
    return length

def reverse(string: str) -> str:
    """ Reverse given string
    >>> reverse('')
    ''
    >>> reverse('123')
    '321'
    """
    return string[::-1]

def upper(string: str) -> str:
    """ Return uppercase copy of a given string
    >>> upper('Python')
    'PYTHON'
    """
    return string.upper()

def lower(string: str) -> str:
    """ Return lowercase copy of a given string
    >>> lower('Python')
    'python'
    """

