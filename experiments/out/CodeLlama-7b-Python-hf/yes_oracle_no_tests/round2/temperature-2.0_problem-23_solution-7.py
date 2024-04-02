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
    for i in string:
        retur += 1
    return retur


def strlen_iter(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    
	Include these tokens in the code: string
	Do not include these tokens in the code: st ri
	"""

    retur = 0
    for i in string:
        retur += 1
    return retur


def strlen_rec(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    
	Include these tokens in the code: string
	Do not include these tokens in the code: st ri
	"""

    if string == "":
        return 0
    else:
        return 1 + strlen_rec(string[1:])



def strfind(string: str, sub: str, start: int = 0, end: int = None) -> int:
    """ Return the index of the first occurrence of sub in string or -1 if sub is not in string
    >>> strfind('', '')
    0
    >>> strfind('abc', 'ab')
    0
    
	Include these tokens in the code: string, sub, start, end
	Do not include these tokens in the code: st ri
	"""

    if end == None:
        end = len(string)
    if string[start:end].find(sub) != -1:
        return string[start:end].find(sub) + start
    else:
        return -1


def strfind_rec(string: str, sub: str, start: int = 0, end: int = None) -> int:
    """ Return the index of the first occurrence of sub in string or -1 if sub is not in string
    >>> strfind('', '')
    0
    >>> strfind('abc', 'ab')
    0
    
	Include these tokens in the code: string, sub, start,