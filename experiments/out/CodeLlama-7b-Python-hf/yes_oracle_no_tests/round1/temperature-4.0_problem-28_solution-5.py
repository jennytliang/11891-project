from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    
	Do not include these tokens in the code: if strings == [] :
	"""
    return ''.join(strings)


def concatenate_with_separator(strings: List[str], separator: str) -> str:
    """ Concatenate list of strings into a single string with separator string between each string
    >>> concatenate_with_separator([], ', ')
    ''
    >>> concatenate_with_separator(['a', 'b', 'c'], '; ')
    'a; b; c'
    
	Do not include these tokens in the code: if strings == [] :
	"""
    return separator.join(strings)


def count_characters(strings: List[str], char: str) -> int:
    """ Count how many times a character appears in a list of strings
    >>> count_characters([], 'a')
    0
    >>> count_characters(['abc', 'abc', 'abc'], 'a')
    9
    >>> count_characters(['abc', 'abc', 'abc'], 'b')
    0
    
	Do not include these tokens in the code: if strings == [] :
	"""
    return sum([s.count(char) for s in strings])


def count_characters_not_in_set(strings: List[str], char_set: set) -> int:
    """ Count how many times a character not in the set appears in a list of strings
    >>> count_characters_not_in_set([], {'a'})
    0
    >>> count_characters_not_in_set(['abc', 'abc', 'abc'], {'a', 'b', 'c'})
    0
    >>> count_characters_not_in_set(['abc', 'abc', 'abc'], {'a', 'b'})
    3
    
	Do not include these tokens in the code: if strings == [] :
	"""
    return sum([s.count(c) for s in strings for c in s if c not in char_set])


def count_distinct_characters(strings: List[str]) -> int:
    """ Count how many distinct characters are in a list of strings
    >>> count_distinct_characters([])
    