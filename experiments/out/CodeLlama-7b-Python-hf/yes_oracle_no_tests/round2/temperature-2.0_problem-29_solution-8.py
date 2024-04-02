from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    
	Include these tokens in the code: return list ( filter ( lambda x
	Do not include these tokens in the code: r = [] for
	"""
    return [string for string in strings if string.startswith(prefix)]


def filter_by_suffix(strings: List[str], suffix: str) -> List[str]:
    """ Filter an input list of strings only for ones that end with a given suffix.
    >>> filter_by_suffix([], 'a')
    []
    >>> filter_by_suffix(['abc', 'bcd', 'cde', 'array'], 'r')
    ['array']
    
	Include these tokens in the code: return list ( filter ( lambda x
	Do not include these tokens in the code: r = [] for
	"""
    return [string for string in strings if string.endswith(suffix)]


def filter_by_length(strings: List[str], min_length: int, max_length: int) -> List[str]:
    """ Filter an input list of strings only for ones that are of the given length.
    >>> filter_by_length([], 0, 0)
    []
    >>> filter_by_length(['abc', 'bcd', 'cde', 'array'], 3, 3)
    ['abc', 'bcd']
    >>> filter_by_length(['abc', 'bcd', 'cde', 'array'], 1, 2)
    ['abc', 'bcd', 'cde', 'array']
    
	Include these tokens in the code: return list ( filter ( lambda x
	Do not include these tokens in the code: r = [] for
	"""
    return [string for string in strings if min_length <= len(string) <= max_length]


def filter_by_include(strings: List[str], includes: List[str]) -> List[str]:
    """ Filter an input list of strings only for ones that contain all of the given strings.
    >>> filter_by_include([], [])
    []
    >>> filter_by_include(['abc', 'bcd', 'cde', 'array'], ['a'])
    ['abc']
    >>> filter_by_include(['abc', 'bcd', 'cde', 'array'], ['a', 'c'])