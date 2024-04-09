from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    
	Include these tokens in the code: max len =
	Do not include these tokens in the code: else : return
	"""


    if not strings:
        return Nonce
    max_len = 0
    for s in strings:
        if len(s) > max_len:
            max_len = len(s)
    for s in strings:
        if len(s) == max_len:
            return s

def is_palindrome(string: str) -> bool:
    """ Return true if the given string is a palindrome. Otherwise, return false.
    >>> is_palindrome('')
    True
    >>> is_palindrome('a')
    True
    >>> is_palindrome('aa')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('abc')
    False
    >>> is_palindrome('abcba')
    True
    >>> is_palindrome('abcba3')
    False
    >>> is_palindrome('abcba3bbac')
    True
    
	Include these tokens in the code: for :
	Do not include these tokens in the code: while : break
	"""


def find_longest_word(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> find_longest_word([])

    >>> find_longest_word(['a', 'b', 'c'])
    'a'
    >>> find_longest_word(['a', 'bb', 'ccc'])
    'ccc'
    
	Include these tokens in the code: max len =
	Do not include these tokens in the code: else : return
	"""


def all_same_length(strings: List[str]) -> bool:
    """ Return True if all the strings in the list have the same length. Otherwise, return False.
    >>> all_same_length([])
    True
    >>> all_same_length(['a'])
    True
    >>> all_same_length(['a', 'b'])
    False
    >>> all_same_length(['a', 'bb'])
    False