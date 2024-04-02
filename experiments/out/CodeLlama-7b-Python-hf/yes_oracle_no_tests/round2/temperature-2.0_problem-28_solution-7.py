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


def reverse(string: str) -> str:
    """ Reverse a string
    >>> reverse('')
    ''
    >>> reverse('a')
    'a'
    >>> reverse('ab')
    'ba'
    >>> reverse('abc')
    'cba'
    
	Include these tokens in the code: return string [ :: - 1 ]
	"""
    return string[::-1]


def replace_vowels(string: str) -> str:
    """ Replace all vowels in a string with '*'
    >>> replace_vowels('')
    ''
    >>> replace_vowels('a')
    '*'
    >>> replace_vowels('ab')
    '*b'
    >>> replace_vowels('abc')
    '*bc'
    
	Include these tokens in the code: return string . replace ( 'a', '*' ) . replace ( 'e', '*' ) . replace ( 'i', '*' ) . replace ( 'o', '*' ) . replace ( 'u', '*' )
	"""
    return string.replace("a", "*").replace("e", "*").replace("i", "*").replace("o", "*").replace("u", "*")


def is_palindrome(string: str) -> bool:
    """ Check if a string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('a')
    True
    >>> is_palindrome('ab')
    False
    >>> is_palindrome('abc')
    False
    >>> is_palindrome('abca')
    True
    >>> is_palindrome('abcba')
    True
    
	Include these tokens in the code: reverse ( string ) == string
	"""
    return reverse(string) == string


def is_pangram(string: str) -> bool:
    """ Check if a string is a pangram
    >>> is_pangram('')
    False
    >>> is_pangram('a')