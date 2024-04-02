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


def filter_by_length(strings: List[str], min_length: int, max_length: int) -> List[str]:
    """ Filter an input list of strings only for ones that have a length in a certain range.
    >>> filter_by_length([], 1, 2)
    []
    >>> filter_by_length(['abc', 'bcd', 'cde', 'array'], 1, 3)
    ['abc', 'bcd', 'cde']
    
	Do not include these tokens in the code: if not strings :
	"""
    return [string for string in strings if min_length <= len(string) <= max_length]


def filter_by_include(strings: List[str], include: str) -> List[str]:
    """ Filter an input list of strings only for ones that include a given substring.
    >>> filter_by_include([], 'a')
    []
    >>> filter_by_include(['abc', 'bcd', 'cde', 'array'], 'r')
    ['array']
    
	Do not include these tokens in the code: if not include or not strings :
	"""
    return [string for string in strings if include in string]


def filter_by_exclude(strings: List[str], exclude: str) -> List[str]:
    """ Filter an input list of strings only for ones that don't include a given substring.
    >>> filter_by_exclude([], '