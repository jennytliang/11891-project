from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    
	Include these tokens in the code: return list ( filter ( lambda x : x .
	"""
    return list(filter(lambda x: x.startswith(prefix), strings))


def filter_by_suffix(strings: List[str], suffix: str) -> List[str]:
    """ Filter an input list of strings only for ones that end with a given suffix.
    >>> filter_by_suffix([], 'a')
    []
    >>> filter_by_suffix(['abc', 'bcd', 'cde', 'array'], 'rray')
    ['array']
    
	Include these tokens in the code: return list ( filter ( lambda x : x .
	"""
    return list(filter(lambda x: x.endswith(suffix), strings))


def filter_by_length(strings: List[str], length: int) -> List[str]:
    """ Filter an input list of strings only for ones that have a given length.
    >>> filter_by_length([], 3)
    []
    >>> filter_by_length(['abc', 'bcd', 'cde', 'array'], 4)
    ['bcd']
    
	Include these tokens in the code: return list ( filter ( lambda x : len ( x ) == length )
	"""
    return list(filter(lambda x: len(x) == length, strings))


def filter_by_contains(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that include a given substring.
    >>> filter_by_contains([], 'a')
    []
    >>> filter_by_contains(['abc', 'bcd', 'cde', 'array'], 'b')
    ['abc', 'bcd', 'array']
    
	Include these tokens in the code: return list ( filter ( lambda x : substring in x )
	"""
    return list(filter(lambda x: substring in x, strings))


def filter_by_condition(strings: List[str], condition) -> List[str]:
    """ Filter an input list of strings only for ones that satisfy a given condition.
    >>> filter_by_condition([], lambda x : len(x) > 3