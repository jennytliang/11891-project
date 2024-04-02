def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    
	Include these tokens in the code: len ( string )
	Do not include these tokens in the code: 0
	"""

    r = len(string)
    return r


def strcat(string1: str, string2: str) -> str:
    """ Return concatenation of given string
    >>> strcat('abc', '')
    'abc'
    >>> strcat('abc', 'def')
    'abcdef'
    
	Include these tokens in the code: +
	Do not include these tokens in the code: '','',''
	"""

    r = string1 + string2
    return r


def strcmp(string1: str, string2: str) -> int:
    """ Return 0 if string1 and string2 are equal,
        -1 if string1 is lexicographically smaller
        than string2, and 1 if string1 is
        lexicographically larger than string2
    >>> strcmp('abc', '')
    -1
    >>> strcmp('abc', 'abc')
    0
    >>> strcmp('abc', 'abcd')
    -1
    >>> strcmp('abc', 'def')
    -1
    >>> strcmp('def', 'abc')
    1
    """

    if string1 == string2:
        r = 0
    elif string1 < string2:
        r = -1
    else:
        r = 1
    return r


def substring(string: str, start: int, end: int) -> str:
    """ Return substring of string from start to end
    Assume start and end are valid indexes for string
    >>> substring('abc', 0, 2)
    'ab'
    >>> substring('abc', 1, 2)
    'bc'
    >>> substring('abc', 0, 1)
    'a'
    >>> substring('abc', 0, 3)
    'abc'
    >>> substring('abc', 2, 3)
    'c'
    """

    r = string[start:end]
    return r


def strfind(string: str, substring: str) -> int:
    """ Return the index of the first occurrence of substring in string
    Return -1 if the substring is not found
