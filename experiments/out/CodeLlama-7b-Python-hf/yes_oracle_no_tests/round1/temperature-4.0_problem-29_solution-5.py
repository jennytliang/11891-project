from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    
	Do not include these tokens in the code: if not prefix or not strings :
	"""
    return list(filter(lambda s: s.startswith(prefix), strings))


def filter_by_suffix(strings: List[str], suffix: str) -> List[str]:
    """ Filter an input list of strings only for ones that end with a given suffix.
    >>> filter_by_suffix([], 'a')
    []
    >>> filter_by_suffix(['abc', 'bcd', 'cde', 'array'], 'rray')
    ['array']
    
	Do not include these tokens in the code: if not suffix or not strings :
	"""
    return list(filter(lambda s: s.endswith(suffix), strings))


def filter_by_symbol(strings: List[str], symbol: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain a given symbol.
    >>> filter_by_symbol([], 'a')
    []
    >>> filter_by_symbol(['abc', 'bcd', 'cde', 'array'], 'r')
    ['array']
    
	Do not include these tokens in the code: if not symbol or not strings :
	"""
    return list(filter(lambda s: symbol in s, strings))


def filter_by_length(strings: List[str], min_length: int, max_length: int) -> List[str]:
    """ Filter an input list of strings only for ones whose length is between
    the given minimum and maximum lengths (inclusive).
    >>> filter_by_length([], 1, 2)
    []
    >>> filter_by_length(['abc', 'bcd', 'cde', 'array'], 2, 4)
    ['abc', 'bcd', 'cde']
    
	Do not include these tokens in the code: if not min_length or not max_length or not strings :
	"""
    return list(filter(lambda s: min_length <= len(s) <= max_length, strings))


def filter_by_letter(strings: List[str], letter: str) -> List[str]:
    """ Filter an input list of