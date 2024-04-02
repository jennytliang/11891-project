from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    
	Include these tokens in the code: return list ( filter ( lambda s : substring in
	"""
    return [sub for sub in strings if substring in sub]


# Pybites solution


def filter_by_substring1(strings: List[str], substring: str) -> List[str]:
    """ 
    Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring1([], 'a')
    []
    >>> filter_by_substring1(['abc', 'bacd', 'cde'], 'a')
    ['abc', 'bacd']
    """
    return [s for s in strings if substring in s]
