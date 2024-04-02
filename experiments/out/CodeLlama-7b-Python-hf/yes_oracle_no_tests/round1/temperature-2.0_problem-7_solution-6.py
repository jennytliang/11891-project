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

    r = list(filter(lambda s: substring.lower() in s.lower(), strings))
    return r


def filter_by_length(strings: List[str], length: int) -> List[str]:
    """ Filter an input list of strings only for ones that have same length as given
    >>> filter_by_length([], 1)
    []
    >>> filter_by_length(['abc', 'bacd', 'cde', 'array'], 3)
    ['abc', 'bacd']
    
	Include these tokens in the code: list ( filter ( lambda s :
	Do not include these tokens in the code: [ string for string in strings if
	"""

    r = list(filter(lambda s: len(s) == length, strings))
    return r


def filter_by_length_range(strings: List[str], min_length: int, max_length: int) -> List[str]:
    """ Filter an input list of strings only for ones that have length in range [min_length, max_length]
    >>> filter_by_length_range([], 1, 10)
    []
    >>> filter_by_length_range(['abc', 'bacd', 'cde', 'array'], 3, 4)
    ['abc', 'bacd']
    
	Include these tokens in the code: list ( filter ( lambda s :
	Do not include these tokens in the code: [ string for string in strings if
	"""

    r = list(filter(lambda s: len(s) >= min_length and len(s) <= max_length, strings))
    return r


def filter_by_condition(strings: List[str], condition: bool) -> List[str]:
    """ Filter an input list of strings only for ones that satisfy given condition
    >>> filter_by_condition([], False)
    []
    >>> filter_by_condition(['abc', 'bacd', 'cde', 'array'], True)
    ['abc', 'bacd', 'cde', 'array']
    
	Include these tokens in the code: list ( filter ( lambda s :
