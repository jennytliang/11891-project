from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    
	Include these tokens in the code: list ( filter ( lambda
	Do not include these tokens in the code: [ s for
	"""


    
    return [s for s in strings if substring in s]


def filter_by_length(strings: List[str], length: int) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_length([], 2)
    []
    >>> filter_by_length(['abc', 'bacd', 'cde', 'array'], 3)
    ['abc', 'bacd', 'array']
    
	Include these tokens in the code: list ( filter ( lambda
	Do not include these tokens in the code: [ s for
	"""

    return [s for s in strings if len(s) == length]


def filter_by_length_and_substring(strings: List[str], length: int, substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_length_and_substring([], 2, 'a')
    []
    >>> filter_by_length_and_substring(['abc', 'bacd', 'cde', 'array'], 3, 'a')
    ['abc', 'bacd']
    
	Include these tokens in the code: list ( filter ( lambda
	Do not include these tokens in the code: [ s for
	"""

    return [s for s in strings if len(s) == length and substring in s]


def filter_by_substring_and_length(strings: List[str], substring: str, length: int) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring_and_length([], 'a', 2)
    []
    >>> filter_by_substring_and_length(['abc', 'bacd', 'cde', 'array'], 'a', 3)
    ['abc', 'bacd']
    
	Include these tokens in the code: list ( filter ( lambda
	Do not include these tokens in the code: [ s for
	"""

    return [s for s in strings if substring in s and len(s