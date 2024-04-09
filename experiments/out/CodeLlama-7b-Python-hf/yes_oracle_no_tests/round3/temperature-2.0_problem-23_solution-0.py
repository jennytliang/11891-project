def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    
	Do not include these tokens in the code: ret ur = 0
	"""
    return len(string)


def strcat(string1: str, string2: str) -> str:
    """ Return concatenation of two given strings
    >>> strcat('abc', 'def')
    'abcdef'
    >>> strcat('abc', '')
    'abc'
    
	Do not include these tokens in the code: ret = ''
	"""
    return string1 + string2


def strinsert(string: str, index: int, char: str) -> str:
    """ Return string with char inserted at given index
    >>> strinsert('abc', 0, 'd')
    'dabc'
    >>> strinsert('abc', 1, 'd')
    'dabc'
    >>> strinsert('abc', 2, 'd')
    'abd'
    >>> strinsert('abc', 3, 'd')
    'abc'
    >>> strinsert('abc', 4, 'd')
    'abc'
    >>> strinsert('abc', 100, 'd')
    'abc'
    
	Do not include these tokens in the code: ret = string
	"""
    return string[:index] + char + string[index:]


def strindex(string: str, char: str, start: int) -> int:
    """ Return the index of the first occurrence of char in string
    starting from start
    >>> strindex('abc', 'a', 0)
    0
    >>> strindex('abc', 'a', 1)
    1
    >>> strindex('abc', 'a', 2)
    2
    >>> strindex('abc', 'a', 3)
    -1
    >>> strindex('abc', 'b', 0)
    1
    >>> strindex('abc', 'b', 1)
    1
    >>> strindex('abc', 'b', 2)
    2
    >>> strindex('abc', 'b', 3)
    -1
    >>> strindex('abc', 'c', 0)
    2
    >>> strindex('abc', 'c', 1)
    2
    >>> strindex('