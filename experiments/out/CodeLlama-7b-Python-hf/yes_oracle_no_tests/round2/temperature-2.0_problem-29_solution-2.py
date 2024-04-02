from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    
	Include these tokens in the code: return list ( filter ( lambda x : x
	Do not include these tokens in the code: r = [ s for s
	"""
    return list(filter(lambda x: x.startswith(prefix), strings))


def filter_by_suffix(strings: List[str], suffix: str) -> List[str]:
    """ Filter an input list of strings only for ones that end with a given suffix.
    >>> filter_by_suffix([], 'a')
    []
    >>> filter_by_suffix(['abc', 'bcd', 'cde', 'array'], 'r')
    ['array']
    
	Include these tokens in the code: return list ( filter ( lambda x : x
	Do not include these tokens in the code: r = [ s for s
	"""
    return list(filter(lambda x: x.endswith(suffix), strings))


def filter_by_length(strings: List[str], minimum: int, maximum: int) -> List[str]:
    """ Filter an input list of strings only for ones that are between a minimum and a maximum length (inclusive).
    >>> filter_by_length([], 1, 2)
    []
    >>> filter_by_length(['a', 'ab', 'abc', 'abcd'], 1, 2)
    ['a', 'ab', 'abc']
    
	Include these tokens in the code: return list ( filter ( lambda x : len ( x )
	Do not include these tokens in the code: r = [ s for s
	"""
    return list(filter(lambda x: minimum <= len(x) <= maximum, strings))


def filter_by_length_greater_than(strings: List[str], n: int) -> List[str]:
    """ Filter an input list of strings only for ones that are longer than a given length.
    >>> filter_by_length_greater_than([], 1)
    []
    >>> filter_by_length_greater_than(['a', 'ab', 'abc', 'abcd'], 2)
    ['abc', 'abcd']
    
	Include these tokens in the code: return list ( filter ( lambda x : len ( x )
	Do not include these tokens in the code: r = [ s