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
    """ Concatenate two strings
    >>> strcat('Hello,', ' world!')
    'Hello, world!'
    >>> strcat('Hello,', '')
    'Hello,'
    
	Include these tokens in the code: +
	Do not include these tokens in the code: 0
	"""

    r = s1 + s2
    return r



def strcmp(s1: str, s2: str) -> int:
    """ Compare two strings
    >>> strcmp('abc', 'abc')
    0
    >>> strcmp('abc', 'abcd')
    -1
    >>> strcmp('abcd', 'abc')
    1
    
	Include these tokens in the code: ==, !=, <, <=, >, >=
	Do not include these tokens in the code: 0
	"""

    if s1 == s2:
        r = 0
    elif s1 != s2:
        r = -1 if s1 < s2 else 1
    return r



def strchr(string: str, character: str) -> str:
    """ Find the first occurrence of character in string
    >>> strchr('Hello, world!', 'o')
    'o'
    >>> strchr('Hello, world!', 'x')
    >>> strchr('Hello, world!', 'H')
    'H'
    
	Include these tokens in the code: in
	Do not include these tokens in the code: 0
	"""

    if character in string:
        r = character
    else:
        r = ''
    return r



def strcpy(destination: str, source: str) -> str:
    """ Copy the contents of source into destination
    >>> strcpy('', 'Hello, world!')
    'Hello, world!'
    >>> strcpy('Hello, world!', '')
    'Hello, world!'
    >>> strcpy('Hello, ', 'World!')
    'Hello, World!'
    
