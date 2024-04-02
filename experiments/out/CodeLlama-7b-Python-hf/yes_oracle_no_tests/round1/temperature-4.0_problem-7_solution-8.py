from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    
	Include these tokens in the code: list (
	Do not include these tokens in the code: _
	"""

    r = []
    for s in strings:
        if substring in s:
            r.append(s)
    return r


def filter_by_length(strings: List[str], min_len: int, max_len: int) -> List[str]:
    """ Filter an input list of strings only for ones that are in given range of characters
    >>> filter_by_length([], 1, 3)
    []
    >>> filter_by_length(['abc', 'bacd', 'cde', 'array'], 2, 4)
    ['abc', 'bacd', 'array']
    
	Include these tokens in the code: list (
	Do not include these tokens in the code: _
	"""

    r = []
    for s in strings:
        if len(s) >= min_len and len(s) <= max_len:
            r.append(s)
    return r


def filter_by_index(strings: List[str], index: int, char: str) -> List[str]:
    """ Filter an input list of strings only for ones that have certain character at given index
    >>> filter_by_index([], 0, 'a')
    []
    >>> filter_by_index(['abc', 'bacd', 'cde', 'array'], 0, 'a')
    ['abc', 'array']
    
	Include these tokens in the code: list (
	Do not include these tokens in the code: _
	"""

    r = []
    for s in strings:
        if s[index] == char:
            r.append(s)
    return r


def filter_by_index_range(strings: List[str], start: int, end: int) -> List[str]:
    """ Filter an input list of strings only for ones that have characters at given range of indices
    >>> filter_by_index_range([], 0, 3)
    []
    >>> filter_by_index_range(['abc', 'bacd', 'cde', 'array'], 2, 4)
    ['cde']
    
	Include these tokens