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
    >>> filter_by_suffix(['abc', 'bcd', 'cde', 'array'], 'rray')
    ['array']
    
	Do not include these tokens in the code: if not suffix or not strings :
	"""
    return list(filter(lambda x: x.endswith(suffix), strings))


def filter_by_length(strings: List[str], min_length: int, max_length: int) -> List[str]:
    """ Filter an input list of strings only for ones that are in given length range.
    >>> filter_by_length([], 1, 2)
    []
    >>> filter_by_length(['abc', 'bcd', 'cde', 'array'], 4, 5)
    ['array']
    
	Do not include these tokens in the code: if not strings :
	"""
    return list(filter(lambda x: len(x) in range(min_length, max_length + 1), strings))


def filter_by_contains(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain a given substring.
    >>> filter_by_contains([], 'a')
    []
    >>> filter_by_contains(['abc', 'bcd', 'cde', 'array'], 'b')
    ['abc', 'bcd', 'cde']
    
	Do not include these tokens in the code: if not substring or not strings :
	"""
    return list(filter(lambda x: substring in x, strings))


def filter_by_condition(strings: List[str], condition: str) -> List[str]:
    """ Filter an input list of strings only for ones that satisfy a given condition.
    >>> filter_