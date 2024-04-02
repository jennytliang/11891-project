from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    
	Do not include these tokens in the code: if not prefix or not strings :
	"""
    return list(filter(lambda x: x.startswith(prefix), strings))


def filter_by_suffix(strings: List[str], suffix: str) -> List[str]:
    """ Filter an input list of strings only for ones that end with a given suffix.
    >>> filter_by_suffix([], 'a')
    []
    >>> filter_by_suffix(['abc', 'bcd', 'cde', 'array'], 'r')
    ['array']
    
	Do not include these tokens in the code: if not suffix or not strings :
	"""
    return list(filter(lambda x: x.endswith(suffix), strings))


def filter_by_length(strings: List[str], min_length: int, max_length: int) -> List[str]:
    """ Filter an input list of strings only for ones that have a length in a given range.
    >>> filter_by_length([], 3, 5)
    []
    >>> filter_by_length(['abc', 'bcd', 'cde', 'array'], 3, 5)
    ['abc', 'bcd', 'cde']
    
	Do not include these tokens in the code: if not min_length or not max_length or not strings :
	"""
    return list(filter(lambda x: min_length <= len(x) <= max_length, strings))


def filter_by_include(strings: List[str], include: str) -> List[str]:
    """ Filter an input list of strings only for ones that include a given substring.
    >>> filter_by_include([], 'a')
    []
    >>> filter_by_include(['abc', 'bcd', 'cde', 'array'], 'r')
    ['array']
    
	Do not include these tokens in the code: if not include or not strings :
	"""
    return list(filter(lambda x: include in x, strings))


def filter_by_exclude(strings: List[str], exclude: str) -> List[str]:
    """ Filter an input list of strings only for ones that exclude a given