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
    """ Return concatenation of given strings
    >>> strcat('abc', '')
    'abc'
    >>> strcat('', 'abc')
    'abc'
    >>> strcat('abc', 'def')
    'abcdef'
    
	Include these tokens in the code: +
	Do not include these tokens in the code: 0
	"""

    r = string1 + string2
    return r


def strcmp(string1: str, string2: str) -> int:
    """ Return 1 if given strings are equal, otherwise return 0
    >>> strcmp('abc', '')
    1
    >>> strcmp('abc', 'abc')
    1
    >>> strcmp('abc', 'abcd')
    0
    >>> strcmp('abc', 'def')
    0
    
	Include these tokens in the code: ==
	Do not include these tokens in the code: 1, 0
	"""

    if string1 == string2:
        r = 1
    else:
        r = 0
    return r


def strrev(string: str) -> str:
    """ Return reversed version of given string
    >>> strrev('')
    ''
    >>> strrev('abc')
    'cba'
    >>> strrev('abcd')
    'dcba'
    >>> strrev('abcde')
    'edcba'
    
	Include these tokens in the code: +, *, len ( string )
	Do not include these tokens in the code: 0
	"""

    r = ''
    for i in range(len(string)):
        r = r + string[len(string) - i - 1]
    return r


def strchr(string: str, char: str) -> str:
    """ Return first occurrence of given character in given string
    >>> strchr('', 'a')
    >>> strchr('abc', 'a')
    'a'
    >>> strchr('abc', 'b