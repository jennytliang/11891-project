def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    
	Include these tokens in the code: return len ( string )
	"""
    return len(string)

def strcat(s1: str, s2: str) -> str:
    """ Concatenate two strings and return the result
    >>> strcat('abc', 'def')
    'abcdef'
    >>> strcat('abc', 'defg')
    'abcdefg'
    
	Include these tokens in the code: string = s1 + s2
	"""
    return s1 + s2

def strinsert(s1: str, s2: str, index: int) -> str:
    """ Insert string s2 into string s1 at index
    >>> strinsert('abc', 'd', 1)
    'adbc'
    >>> strinsert('abc', 'd', 2)
    'abdc'
    
	Include these tokens in the code: string = s1[:index] + s2 + s1[index:]
	"""
    return s1[:index] + s2 + s1[index:]

def strinstr(string: str, substring: str) -> bool:
    """ Return True if substring is in string, False otherwise
    >>> strinstr('abc', 'c')
    True
    >>> strinstr('abc', 'd')
    False
    
	Include these tokens in the code: return substring in string
	"""
    return substring in string

def strfind(string: str, substring: str) -> int:
    """ Return index of first occurrence of substring in string
    >>> strfind('abcabc', 'c')
    2
    >>> strfind('abcabc', 'd')
    -1
    
	Include these tokens in the code: return string.find(substring)
	"""
    return string.find(substring)

def strchar(string: str, index: int) -> str:
    """ Return character at index in string
    >>> strchar('abc', 1)
    'b'
    >>> strchar('abc', 2)
    'c'
    
	Include these tokens in the code: return string[index]
	"""
    return string[index]

def strmkupper(string: str)