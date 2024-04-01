from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    
	Include these tokens in the code: :(
	Do not include these tokens in the code: 0 :
	"""


    return [s for s in string]


def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_suffixes('abc')
    ['c', 'bc', 'abc']
    
	Include these tokens in the code: :(
	Do not include these tokens in the code: 0 :
	"""


    return [s for s in string]


def reverse_string(string: str) -> str:
    """ Return a reversed version of the input string
    >>> reverse_string('abc')
    'cba'
    
	Include these tokens in the code: :(
	Do not include these tokens in the code: 0 :
	"""


    return string[::-1]


def is_palindrome(string: str) -> bool:
    """ Return True if the input string is a palindrome
    >>> is_palindrome('noon')
    True
    >>> is_palindrome('racecar')
    True
    
	Include these tokens in the code: :(
	Do not include these tokens in the code: 0 :
	"""


    return string == reverse_string(string)


def is_pangram(string: str) -> bool:
    """ Return True if the input string is a pangram
    >>> is_pangram('The quick brown fox jumps over the lazy dog.')
    True
    >>> is_pangram('abc')
    False
    
	Include these tokens in the code: :(
	Do not include these tokens in the code: 0 :
	"""


    return len(set(string.lower())) == 26


def list_rotate(lst: List, n: int) -> List:
    """ Rotate the input list by n elements
    >>> list_rotate([1, 2, 3, 4, 5, 6], 2)
    [3, 4, 5, 6, 1, 2]
    
	Include these tokens in the code: