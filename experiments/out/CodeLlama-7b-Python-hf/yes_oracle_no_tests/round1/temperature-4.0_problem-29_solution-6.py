from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    
	Do not include these tokens in the code: if not prefix or not strings :
	"""
    return [string for string in strings if string.startswith(prefix)]


def filter_by_suffix(strings: List[str], suffix: str) -> List[str]:
    """ Filter an input list of strings only for ones that end with a given suffix.
    >>> filter_by_suffix([], 'a')
    []
    >>> filter_by_suffix(['abc', 'bcd', 'cde', 'array'], 'rray')
    ['array']
    
	Do not include these tokens in the code: if not suffix or not strings :
	"""
    return [string for string in strings if string.endswith(suffix)]


def filter_by_length(strings: List[str], min_len: int, max_len: int) -> List[str]:
    """ Filter an input list of strings only for ones that have a length between a given range.
    >>> filter_by_length([], 2, 4)
    []
    >>> filter_by_length(['abc', 'bcd', 'cde', 'array'], 2, 4)
    ['abc', 'bcd', 'cde']
    
	Do not include these tokens in the code: if not strings :
	"""
    return [string for string in strings if min_len <= len(string) <= max_len]


def filter_by_include(strings: List[str], includes: List[str]) -> List[str]:
    """ Filter an input list of strings only for ones that include all given substrings.
    >>> filter_by_include([], ['a'])
    []
    >>> filter_by_include(['abc', 'bcd', 'cde', 'array'], ['b', 'c'])
    ['bcd', 'cde']
    
	Do not include these tokens in the code: if not strings or not includes :
	"""
    return [string for string in strings if all(include in string for include in includes)]


def filter_by_exclude(strings: List[str], excludes: List[str]) -> List[str]:
    """ Filter an input list of strings only for ones that