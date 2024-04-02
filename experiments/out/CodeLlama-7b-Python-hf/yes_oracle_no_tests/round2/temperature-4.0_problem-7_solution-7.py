from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    
	Include these tokens in the code: return list ( filter ( lambda
	Do not include these tokens in the code: r = [] for
	"""
    return list(filter(lambda x: substring in x, strings))


def filter_by_length(strings: List[str], minimum: int, maximum: int) -> List[str]:
    """ Filter an input list of strings only for ones that have length between minimum and maximum
    >>> filter_by_length([], 1, 10)
    []
    >>> filter_by_length(['abc', 'bacd', 'cde', 'array'], 1, 3)
    ['abc', 'bacd', 'cde']
    
	Include these tokens in the code: return list ( filter ( lambda
	Do not include these tokens in the code: r = [] for
	"""
    return list(filter(lambda x: len(x) > minimum and len(x) < maximum, strings))


def filter_by_ends_with(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that end with given substring
    >>> filter_by_ends_with([], 'a')
    []
    >>> filter_by_ends_with(['abc', 'bacd', 'cde', 'array'], 'r')
    ['array']
    
	Include these tokens in the code: return list ( filter ( lambda
	Do not include these tokens in the code: r = [] for
	"""
    return list(filter(lambda x: x.endswith(substring), strings))


def filter_by_starts_with(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with given substring
    >>> filter_by_starts_with([], 'a')
    []
    >>> filter_by_starts_with(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'array']
    
	Include these tokens in the code: return list ( filter ( lambda
	Do not include these tokens in the code: r = [] for
	"""
    return list(filter(lambda x: x.startswith(substring), strings))


def filter_by_include