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
    """ Filter an input list of strings only for ones that have length equal to a given length
    >>> filter_by_length([], 1)
    []
    >>> filter_by_length(['abc', 'bacd', 'cde', 'array'], 2)
    ['abc', 'bacd', 'cde']
    
	Include these tokens in the code: return list ( filter ( lambda s : len (s) == length
    """
    return list(filter(lambda s: len(s) == length, strings))


def filter_by_substring_and_length(strings: List[str], substring: str, length: int) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring and have length equal to a given length
    >>> filter_by_substring_and_length([], 'a', 2)
    []
    >>> filter_by_substring_and_length(['abc', 'bacd', 'cde', 'array'], 'a', 2)
    ['abc', 'bacd']
    
	Include these tokens in the code: return list ( filter ( lambda s : substring in s and len (s) == length
    """
    return list(filter(lambda s: substring in s and len(s) == length, strings))


def filter_by_substring_or_length(strings: List[str], substring: str, length: int) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring or have length equal to a given length
    >>> filter_by_substring_or_length([], 'a', 2)
    []
    >>> filter_by_substring_or_length(['abc', 'bacd', 'cde', 'array'], 'a', 2)
    ['abc', 'bacd', 'cde']
    
	Include these tokens in the code: return list ( filter ( lambda s : substring in s or len (s) == length
    """