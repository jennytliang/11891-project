from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    
	Include these tokens in the code: x
	Do not include these tokens in the code: s
	"""

    return list(filter(l -> l.startswith(prefix), strings))


def filter_by_suffix(strings: List[str], suffix: str) -> List[str]:
    """ Filter an input list of strings only for ones that end with a given suffix.
    >>> filter_by_suffix([], 'a')
    []
    >>> filter_by_suffix(['abc', 'bcd', 'cde', 'array'], 'rray')
    ['array']
    
	Include these tokens in the code: x
	Do not include these tokens in the code: s
	"""

    return list(filter(l -> l.endswith(suffix), strings))


def filter_by_length(strings: List[str], length: int) -> List[str]:
    """ Filter an input list of strings only for ones that have a given length.
    >>> filter_by_length([], 3)
    []
    >>> filter_by_length(['abc', 'bcd', 'cde', 'array'], 5)
    ['array']
    
	Include these tokens in the code: x
	Do not include these tokens in the code: s
	"""

    return list(filter(l -> len(l) == length, strings))


def filter_by_include(strings: List[str], include: str) -> List[str]:
    """ Filter an input list of strings only for ones that include a given substring.
    >>> filter_by_include([], 'a')
    []
    >>> filter_by_include(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    
	Include these tokens in the code: x
	Do not include these tokens in the code: s
	"""

    return list(filter(l -> l.__contains__(include), strings))


def filter_by_exclude(strings: List[str], exclude: str) -> List[str]:
    """ Filter an input list of strings only for ones that do not include a given substring.
    >>> filter_by_exclude([], 'a')
    []
    >>> filter_by_