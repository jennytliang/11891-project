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
    return [x for x in strings if x.startswith(prefix)]


def filter_by_suffix(strings: List[str], suffix: str) -> List[str]:
    """ Filter an input list of strings only for ones that end with a given suffix.
    >>> filter_by_suffix([], 'a')
    []
    >>> filter_by_suffix(['abc', 'bcd', 'cde', 'array'], 'r')
    ['array']
    
	Include these tokens in the code: return list ( filter ( lambda x
	Do not include these tokens in the code: r = [] for
	"""
    return [x for x in strings if x.endswith(suffix)]


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain a given substring.
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bcd', 'cde', 'array'], 'r')
    ['array']
    
	Include these tokens in the code: return list ( filter ( lambda x
	Do not include these tokens in the code: r = [] for
	"""
    return [x for x in strings if substring in x]


def filter_by_length(strings: List[str], min_len: int, max_len: int) -> List[str]:
    """ Filter an input list of strings only for ones that have a length between min_len and max_len.
    >>> filter_by_length([], 3, 7)
    []
    >>> filter_by_length(['abc', 'bcd', 'cde', 'array'], 3, 7)
    ['abc', 'bcd', 'cde']
    
	Include these tokens in the code: return list ( filter ( lambda x
	Do not include these tokens in the code: r = [] for
	"""
    return [x for x in strings if len(x) >= min_len and len(x) <= max_len]


def filter_by_multi