from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    
	Include these tokens in the code: return list ( filter ( lambda
	Do not include these tokens in the code: r = [] for
	"""
    return [string for string in strings if substring in string]


def filter_by_length(strings: List[str], length: int) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_length([], 2)
    []
    >>> filter_by_length(['abc', 'bacd', 'cde', 'array'], 2)
    ['abc', 'bacd', 'cde']
    
	Include these tokens in the code: return list ( filter ( lambda
	Do not include these tokens in the code: r = [] for
	"""
    return [string for string in strings if len(string) == length]


def filter_by_multiple_conditions(strings: List[str], substring: str, length: int) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_multiple_conditions([], 'a', 2)
    []
    >>> filter_by_multiple_conditions(['abc', 'bacd', 'cde', 'array'], 'a', 2)
    ['abc', 'bacd']
    
	Include these tokens in the code: return list ( filter ( lambda
	Do not include these tokens in the code: r = [] for
	"""
    return [string for string in strings if substring in string and len(string) == length]


def filter_by_multiple_conditions_with_not(strings: List[str], substring: str, length: int) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_multiple_conditions_with_not([], 'a', 2)
    []
    >>> filter_by_multiple_conditions_with_not(['abc', 'bacd', 'cde', 'array'], 'a', 2)
    ['abc', 'bacd']
    
	Include these tokens in the code: return list ( filter ( lambda
	Do not include these tokens in the code: r = [] for
	"""
    return [string for string in