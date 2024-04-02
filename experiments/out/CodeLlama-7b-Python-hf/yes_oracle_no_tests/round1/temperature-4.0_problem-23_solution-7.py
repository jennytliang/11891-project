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


def strcat(s1: str, s2: str) -> str:
    """ Return concatenation of given strings
    >>> strcat('abc', '')
    'abc'
    >>> strcat('', 'abc')
    'abc'
    >>> strcat('abc', 'def')
    'abcdef'
    """

    r = s1 + s2
    return r


def strcmp(s1: str, s2: str) -> int:
    """ Return -1 if s1 < s2, else return 1 if s1 > s2, else return 0
    >>> strcmp('abc', 'abc')
    0
    >>> strcmp('abc', 'def')
    -1
    >>> strcmp('def', 'abc')
    1
    """

    r = 0
    if s1 > s2:
        r = 1
    elif s1 < s2:
        r = -1
    return r


def strfind(s1: str, s2: str) -> int:
    """ Return index of s2 in s1, else return -1
    >>> strfind('abcdef', 'abc')
    0
    >>> strfind('abcdef', 'bc')
    1
    >>> strfind('abcdef', 'ef')
    4
    >>> strfind('abcdef', 'f')
    5
    >>> strfind('abcdef', 'fg')
    -1
    """

    r = s1.find(s2)
    return r


def strsub(s1: str, i: int, j: int) -> str:
    """ Return substring of s1 starting at i and ending at j
    >>> strsub('abcdef', 3, 5)
    'def'
    """

    r = s1[i:j]
    return r


def strsub1(s1: str, i: int) -> str:
    """ Return substring of s1 starting at i
    >>> strsub1('abcdef', 3)
    'def'
    """

   