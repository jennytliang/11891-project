from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    
	Include these tokens in the code: list ( filter ( lambda s :
	Do not include these tokens in the code: [ string for string in strings if
	"""

    r = [string for string in strings if substring in string]
    return r


def filter_by_length(strings: List[str], length: int) -> List[str]:
    """ Filter an input list of strings only for ones that have given length
    >>> filter_by_length([], 1)
    []
    >>> filter_by_length(['abc', 'bacd', 'cde', 'array'], 2)
    ['abc', 'bacd']
    
	Include these tokens in the code: list ( filter ( lambda s :
	Do not include these tokens in the code: [ string for string in strings if
	"""

    r = [string for string in strings if len(string) == length]
    return r


def filter_by_substring_and_length(strings: List[str], substring: str, length: int) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring and have given length
    >>> filter_by_substring_and_length([], 'a', 1)
    []
    >>> filter_by_substring_and_length(['abc', 'bacd', 'cde', 'array'], 'a', 2)
    ['abc', 'bacd']
    
	Include these tokens in the code: list ( filter ( lambda s :
	Do not include these tokens in the code: [ string for string in strings if
	"""

    r = [string for string in strings if substring in string and len(string) == length]
    return r


def filter_by_substring_or_length(strings: List[str], substring: str, length: int) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring or have given length
    >>> filter_by_substring_or_length([], 'a', 1)
    []
    >>> filter_by_substring_or_length(['abc', 'bacd', 'cde', 'array'], 'a', 2)
    ['abc', 'bacd', 'array']
    
	Include these tokens in the code: list ( filter ( lambda s :
	