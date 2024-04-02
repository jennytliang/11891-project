from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    return r


def count_char(string: str, char: str) -> int:
    """ Count the number of instances of a character in a string
    >>> count_char('1111', '1')
    4
    >>> count_char('abcabcabc', 'a')
    3
    >>> count_char('aaa', 'b')
    0
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    return r


def find_char(string: str, char: str) -> int:
    """ Find the index of the first character in a string
    >>> find_char('abcabcabc', 'a')
    0
    >>> find_char('abcabcabc', 'b')
    1
    >>> find_char('abcabcabc', 'c')
    2
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    return r


def find_char_reverse(string: str, char: str) -> int:
    """ Find the index of the last character in a string
    >>> find_char_reverse('abcabcabc', 'a')
    5
    >>> find_char_reverse('abcabcabc', 'b')
    6
    >>> find_char_reverse('abcabcabc', 'c')
    7
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    return r


def is_palindrome_iterative(string: str) -> bool:
    """ Check whether a string is a palindrome
    >>> is_palindrome_iterative('')
    True
    >>> is_palindrome_iterative('a')
    True
    >>> is_palindrome_iterative('aa')
    True
    >>> is_palindrome_iterative('ab')
    False
    >>> is_palindrome_iterative('abc')
    False
    >>> is_palindrome_iterative('abcba')
    True
    >>> is_pal