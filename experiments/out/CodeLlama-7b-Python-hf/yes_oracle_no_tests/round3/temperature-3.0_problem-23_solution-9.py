def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    
	Include these tokens in the code: return len ( string )
	"""

    return len(string)


###############################################################################


def strcat(string1: str, string2: str) -> str:
    """ Concatenate given strings
    >>> strcat('', '')
    ''
    >>> strcat('abc', '123')
    'abc123'
    
	Include these tokens in the code: string1 + string2
	"""

    return string1 + string2


###############################################################################


def strcmp(string1: str, string2: str) -> int:
    """ Compare given strings
    >>> strcmp('abc', 'abc')
    0
    >>> strcmp('abc', '123')
    1
    >>> strcmp('123', 'abc')
    -1
    
	Include these tokens in the code: if string1 == string2: return 0 else if string1 < string2: return -1 else return 1
	"""

    if string1 == string2:
        return 0
    elif string1 < string2:
        return -1
    else:
        return 1


###############################################################################


def strchr(string: str, char: str) -> str:
    """ Find first occurrence of given character in string
    >>> strchr('', 'a')
    >>> strchr('abc', 'a')
    'a'
    >>> strchr('abc', 'd')
    >>> strchr('abc', 'c')
    'c'
    
	Include these tokens in the code: string.find(char)
	"""

    return string[string.find(char)]


###############################################################################


def strcpy(string: str) -> str:
    """ Copy given string
    >>> strcpy('')
    ''
    >>> strcpy('abc')
    'abc'
    
	Include these tokens in the code: string
	"""

    return string


###############################################################################


def strdup(string: str) -> str:
    """ Dup