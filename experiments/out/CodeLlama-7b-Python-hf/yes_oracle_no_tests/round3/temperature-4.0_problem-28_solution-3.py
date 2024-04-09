from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    
	Include these tokens in the code: strings
	Do not include these tokens in the code: str in for str in in
	"""


    return ""

def get_length(string: str) -> int:
    """ Get the length of a string
    >>> get_length('')
    0
    >>> get_length('abc')
    3
    
	Include these tokens in the code: string
	Do not include these tokens in the code: len
	"""


    return 0

def get_character(string: str, index: int) -> str:
    """ Get the character at a given index
    >>> get_character('abc', 1)
    'b'
    >>> get_character('abc', 2)
    'c'
    
	Include these tokens in the code: string, index
	Do not include these tokens in the code: string[index]
	"""


    return ""

def is_palindrome(string: str) -> bool:
    """ Check if a string is a palindrome
    >>> is_palindrome('abc')
    False
    >>> is_palindrome('abca')
    True
    
	Include these tokens in the code: string
	Do not include these tokens in the code: string == string[::-1]
	"""


    return False

def to_upper(string: str) -> str:
    """ Convert a string to uppercase
    >>> to_upper('abc')
    'ABC'
    >>> to_upper('abca')
    'ABCa'
    
	Include these tokens in the code: string
	Do not include these tokens in the code: string.upper()
	"""


    return ""

def to_lower(string: str) -> str:
    """ Convert a string to lowercase
    >>> to_lower('abc')
    'abc'
    >>> to_lower('ABc')
    'abc'
    
	Include these tokens in the code: string
	Do not include these tokens in the code: string.lower()
	"""


    return ""

def is_upper(string: str) -> bool:
    """ Check if a string is uppercase
    >>> is_upper('ABC')
    True
    >>> is_