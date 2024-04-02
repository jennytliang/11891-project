from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    
	Include these tokens in the code: return list ( filter ( lambda s : substring in
	"""
    return list(filter(lambda s: substring in s, strings))


def filter_by_length(strings: List[str], length: int) -> List[str]:
    """ Filter an input list of strings only for ones that have length equal to given length
    >>> filter_by_length([], 0)
    []
    >>> filter_by_length(['abc', 'bacd', 'cde', 'array'], 4)
    ['abc', 'bacd']
    
	Include these tokens in the code: return list ( filter ( lambda s : len ( s ) ==
	"""
    return list(filter(lambda s: len(s) == length, strings))


def filter_by_length_range(strings: List[str], min_length: int, max_length: int) -> List[str]:
    """ Filter an input list of strings only for ones that have length in the range of given lengths
    >>> filter_by_length_range([], 0, 10)
    []
    >>> filter_by_length_range(['abc', 'bacd', 'cde', 'array'], 4, 6)
    ['abc', 'bacd']
    
	Include these tokens in the code: return list ( filter ( lambda s : len ( s ) >=
	"""
    return list(filter(lambda s: len(s) >= min_length and len(s) <= max_length, strings))


def filter_by_length_range_and_substring(strings: List[str], min_length: int, max_length: int, substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that have length in the range of given lengths
    and contain given substring
    >>> filter_by_length_range_and_substring([], 0, 10, 'a')
    []
    >>> filter_by_length_range_and_substring(['abc', 'bacd', 'cde', 'array'], 4, 6, 'a')
    ['abc', 'bacd']
    
	Include these tokens in the code: return list ( filter ( lambda s