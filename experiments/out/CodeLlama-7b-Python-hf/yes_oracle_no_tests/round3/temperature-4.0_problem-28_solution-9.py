from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    
	Include these tokens in the code: return " ". join ( strings )
	"""
    return " ".join(strings)


def remove_duplicates(strings: List[str]) -> List[str]:
    """ Remove duplicates from list of strings
    >>> remove_duplicates([])
    []
    >>> remove_duplicates(['a', 'b', 'a'])
    ['a', 'b']
    
	Include these tokens in the code: return list ( set ( strings ) )
    """
    return list(set(strings))


def reverse(string: str) -> str:
    """ Reverse a string
    >>> reverse('')
    ''
    >>> reverse('a')
    'a'
    >>> reverse('ab')
    'ba'
    
	Include these tokens in the code: return string [ :: - 1 ]
	"""
    return string[::-1]


def is_palindrome(string: str) -> bool:
    """ Check if a string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('a')
    True
    >>> is_palindrome('ab')
    False
    >>> is_palindrome('abba')
    True
    
	Include these tokens in the code: return string == reverse ( string ) 
	"""
    return string == reverse(string)


def count_characters(string: str) -> int:
    """ Count characters in a string
    >>> count_characters('')
    0
    >>> count_characters('a')
    1
    >>> count_characters('ab')
    2
    
	Include these tokens in the code: return len ( string ) 
	"""
    return len(string)


def is_empty(string: str) -> bool:
    """ Check if a string is empty
    >>> is_empty('')
    True
    >>> is_empty('a')
    False
    
	Include these tokens in the code: return len ( string ) == 0
	"""
    return len(string) == 0


def is_alphanumeric(string: str) -> bool:
    """ Check if a string