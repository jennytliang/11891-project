from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    
	Include these tokens in the code: list ( filter ( lambda
	Do not include these tokens in the code: [ x for
	"""

    r = []
    for s in strings:
        if s.startswith(prefix):
            r.append(s)
    return r


def filter_by_suffix(strings: List[str], suffix: str) -> List[str]:
    """ Filter an input list of strings only for ones that end with a given suffix.
    >>> filter_by_suffix([], 'a')
    []
    >>> filter_by_suffix(['abc', 'bcd', 'cde', 'array'], 'rray')
    ['array']
    
	Include these tokens in the code: list ( filter ( lambda
	Do not include these tokens in the code: [ x for
	"""

    r = []
    for s in strings:
        if s.endswith(suffix):
            r.append(s)
    return r


def filter_by_length(strings: List[str], min_length: int, max_length: int) -> List[str]:
    """ Filter an input list of strings only for ones that have a length between given bounds.
    >>> filter_by_length([], 2, 4)
    []
    >>> filter_by_length(['abc', 'bcd', 'cde', 'array'], 2, 4)
    ['abc', 'bcd', 'cde']
    
	Include these tokens in the code: list ( filter ( lambda
	Do not include these tokens in the code: [ x for
	"""

    r = []
    for s in strings:
        if min_length <= len(s) <= max_length:
            r.append(s)
    return r


def filter_by_regex(strings: List[str], regex: str) -> List[str]:
    """ Filter an input list of strings only for ones that match a given pattern.
    >>> filter_by_regex([], 'a')
    []
    >>> filter_by_regex(['abc', 'bcd', 'cde', 'array'], '[bc][cd][de]')
    ['bcd']
    
	Include these tokens in the code: list ( filter ( lambda
