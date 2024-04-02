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


def filter_by_length(strings: List[str], min_length: int, max_length: int) -> List[str]:
    """ Filter an input list of strings only for ones that have length in given range
    >>> filter_by_length([], 1, 2)
    []
    >>> filter_by_length(['abc', 'bacd', 'cde', 'array'], 1, 3)
    ['abc', 'bacd', 'array']
    
	Include these tokens in the code: list (
	Do not include these tokens in the code: _
	"""

    r = []
    for s in strings:
        if min_length <= len(s) <= max_length:
            r.append(s)
    return r


def filter_by_length_and_substring(strings: List[str], min_length: int, max_length: int, substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that have length in given range and contain given substring
    >>> filter_by_length_and_substring([], 1, 2, 'a')
    []
    >>> filter_by_length_and_substring(['abc', 'bacd', 'cde', 'array'], 1, 3, 'a')
    ['abc', 'bacd']
    
	Include these tokens in the code: list (
	Do not include these tokens in the code: _
	"""

    r = []
    for s in strings:
        if min_length <= len(s) <= max_length and substring in s:
            r.append(s)
    return r


def filter_by_substring_and_length(strings: List[str], min_length: int, max_length: int, substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring and have length in given range
    >>> filter_by_substring_and_length([], 1, 