from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    
	Include these tokens in the code: return " ". join ( strings )
	Do not include these tokens in the code: result : str = ""
	"""
    return " ".join(strings)


def concatenate_with_separators(strings: List[str], separators: List[str]) -> str:
    """ Concatenate list of strings into a single string with separators between each string
    >>> concatenate_with_separators([], [])
    ''
    >>> concatenate_with_separators(['a', 'b', 'c'], [',', '.'])
    'a, b, c'
    
	Include these tokens in the code: return " ". join ( strings )
	Do not include these tokens in the code: result : str = ""
	"""
    return " ".join(strings)


def count_substring(string: str, substring: str) -> int:
    """ Count the number of substrings in a string
    >>> count_substring('', '')
    0
    >>> count_substring('abc', '')
    3
    >>> count_substring('abc', 'a')
    1
    >>> count_substring('abc', 'b')
    1
    >>> count_substring('abc', 'c')
    1
    >>> count_substring('abc', 'ab')
    1
    >>> count_substring('abc', 'bc')
    1
    >>> count_substring('abc', 'bc')
    1
    >>> count_substring('abbc', 'bc')
    2
    >>> count_substring('abbc', 'abc')
    1
    >>> count_substring('abbc', 'ab')
    1
    >>> count_substring('abbc', 'bc')
    2
    >>> count_substring('abbc', 'abc')
    1
    >>> count_substring('abbc', 'ab')
    1
    """
    return string.count(substring)


def find_string(string: str, target: str) -> int:
    """ Find the first position of a substring in a string
    >>> find_string('', '')
    -1
    >>> find_string('abc', '')
    -1
    >>> find_string('abc', 'a')
    0
    >>> find_string('abc', 'b')
    1
    >>> find_