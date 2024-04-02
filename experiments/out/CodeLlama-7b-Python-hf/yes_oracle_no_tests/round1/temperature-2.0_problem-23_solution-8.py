def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    
	Include these tokens in the code: return len ( string )
	"""
    return len(string)


def strcat(string1: str, string2: str) -> str:
    """ Concatenate two strings
    >>> strcat('abc', 'def')
    'abcdef'
    
	Include these tokens in the code: string1 + string2
	"""
    return string1 + string2


def strcatn(string1: str, string2: str) -> str:
    """ Concatenate two strings, with newline character
    >>> strcatn('abc', 'def')
    'abc\ndef'
    
	Include these tokens in the code: string1 + '\n' + string2
	"""
    return string1 + '\n' + string2


def strinsert(string1: str, string2: str, index: int) -> str:
    """ Insert the string into the given index of the given string
    >>> strinsert('abc', 'd', 1)
    'adbc'
    
	Include these tokens in the code: string1[ : index ] + string2 + string1[ index : ]
	"""
    return string1[:index] + string2 + string1[index:]


def strreplace(string1: str, string2: str, string3: str) -> str:
    """ Replace the substring with the given string
    >>> strreplace('abcabc', 'abc', 'ABC')
    'ABCABC'
    
	Include these tokens in the code: string1.replace(string2, string3)
	"""
    return string1.replace(string2, string3)


def strindex(string1: str, string2: str) -> int:
    """ Find the index of the substring in the given string
    >>> strindex('abcabc', 'abc')
    0
    
	Include these tokens in the code: string1.index(string2)
	"""
    return string1.index(string2)


def strcount(string1: str, string2: str) -> int:
    """ Count the number of occurence of the substring in the given string
    >>> strcount('abcabcabc', 'abc