def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    
	Include these tokens in the code: string
	Do not include these tokens in the code: st ri
	"""


    retur = 0
    for i in range(len(string)):
        if string[i] != ' ':
            retur += 1
    return retur




def strcat(string1: str, string2: str) -> str:
    """ Return concatenation of given strings
    >>> strcat('abc', '123')
    'abc123'
    >>> strcat('abc', '123')
    'abc123'
    
	Include these tokens in the code: string1 string2 +
    
	Do not include these tokens in the code: string st ri
	"""
    return string1 + string2




def strcopy(string1: str, string2: str) -> str:
    """ Return copy of given string
    >>> strcopy('abc', '123')
    'abc'
    >>> strcopy('abc', '123')
    'abc'
    
	Include these tokens in the code: string1 string2
	Do not include these tokens in the code: string st ri
	"""
    return string1




def strcmp(string1: str, string2: str) -> int:
    """ Return 0 if given strings are equal, 1 if they are not equal
    >>> strcmp('abc', '123')
    1
    >>> strcmp('abc', 'abc')
    0
    
	Include these tokens in the code: string1 string2
	Do not include these tokens in the code: string st ri
	"""
    if string1 == string2:
        return 0
    else:
        return 1




def strget(string: str, index: int) -> str:
    """ Return character at given index
    >>> strget('abc', 0)
    'a'
    >>> strget('abc', 1)
    'b'
    
	Include these tokens in the code: string index
	Do not include these tokens in the code: string st ri
	"""
    return string[index]




def strset(string: str, index: int,