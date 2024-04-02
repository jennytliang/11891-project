from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    
	Include these tokens in the code: return list ( filter ( lambda s : substring in
	"""
    return list(filter(lambda s: substring in s, strings))


def filter_by_length(strings: List[str], length: int) -> List[str]:
    """ Filter an input list of strings only for ones that are of given length
    >>> filter_by_length([], 0)
    []
    >>> filter_by_length(['abc', 'bacd', 'cde', 'array'], 0)
    ['abc', 'bacd', 'cde', 'array']
    >>> filter_by_length(['abc', 'bacd', 'cde', 'array'], 4)
    ['abc', 'bacd', 'array']
    
	Include these tokens in the code: return list ( filter ( lambda s : len ( s ) == length
    """
    return list(filter(lambda s: len(s) == length, strings))


def filter_by_starts_with(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with given substring
    >>> filter_by_starts_with([], 'a')
    []
    >>> filter_by_starts_with(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'array']
    
	Include these tokens in the code: return list ( filter ( lambda s : s.startswith
    """
    return list(filter(lambda s: s.startswith(substring), strings))


def filter_by_ends_with(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that end with given substring
    >>> filter_by_ends_with([], 'a')
    []
    >>> filter_by_ends_with(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd']
    
	Include these tokens in the code: return list ( filter ( lambda s : s.endswith
    """
    return list(filter(lambda s: s.endswith(substring), strings))


def filter_by_include(