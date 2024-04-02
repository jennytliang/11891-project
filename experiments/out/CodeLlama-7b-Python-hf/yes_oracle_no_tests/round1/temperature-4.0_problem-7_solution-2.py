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

    r = [s for s in strings if substring in s]
    return r


def filter_by_length(strings: List[str], min_len: int, max_len: int) -> List[str]:
    """ Filter an input list of strings only for ones that are in given range of length
    >>> filter_by_length([], 1, 10)
    []
    >>> filter_by_length(['abc', 'bacd', 'cde', 'array'], 1, 4)
    ['abc', 'bacd']
    
	Include these tokens in the code: list (
	Do not include these tokens in the code: _
	"""

    r = [s for s in strings if len(s) >= min_len and len(s) <= max_len]
    return r


def filter_by_multiple_conditions(strings: List[str], substring: str, min_len: int,
                                  max_len: int) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring and are in given range of length
    >>> filter_by_multiple_conditions([], 'a', 1, 10)
    []
    >>> filter_by_multiple_conditions(['abc', 'bacd', 'cde', 'array'], 'a', 1, 4)
    ['abc', 'bacd']
    
	Include these tokens in the code: list (
	Do not include these tokens in the code: _
	"""

    r = [s for s in strings if len(s) >= min_len and len(s) <= max_len and substring in s]
    return r


def filter_by_multiple_conditions_advanced(strings: List[str], substring: str,
                                           min_len: int, max_len: int) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring and are in given range of length
    >>> filter_by_multiple_conditions_advanced([], 'a', 1, 10)
    []
    >>> filter_by