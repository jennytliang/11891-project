from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    
	Include these tokens in the code: return list ( filter ( lambda s : substring in
	"""
    return [string for string in strings if substring in string]


def filter_by_length(strings: List[str], length: int) -> List[str]:
    """ Filter an input list of strings only for ones with given length
    >>> filter_by_length([], 2)
    []
    >>> filter_by_length(['abc', 'bacd', 'cde', 'array'], 2)
    ['abc', 'bacd', 'array']
    
	Include these tokens in the code: return list ( filter ( lambda s : len ( s ) ==
	"""
    return [string for string in strings if len(string) == length]


def filter_by_substring_length(strings: List[str], substring_length: int) -> List[str]:
    """ Filter an input list of strings only for ones with substrings of given length
    >>> filter_by_substring_length([], 2)
    []
    >>> filter_by_substring_length(['abc', 'bacd', 'cde', 'array'], 2)
    ['bacd', 'array']
    
	Include these tokens in the code: return list ( filter ( lambda s : len ( filter (
	"""
    return [string for string in strings if len(list(filter(lambda x: len(x) == substring_length, string))) > 0]


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with given prefix
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'array']
    
	Include these tokens in the code: return list ( filter ( lambda s : s.startswith (
	"""
    return [string for string in strings if string.startswith(prefix)]


def filter_by_suffix(strings: List[str], suffix: str) -> List[str]:
    """ Filter an input list of strings only for ones that end with given suffix
   