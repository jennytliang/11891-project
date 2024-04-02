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

    r = list(filter(lambda s: substring in s, strings))
    return r


def filter_by_length(strings: List[str], length: int) -> List[str]:
    """ Filter an input list of strings only for ones that have given length
    >>> filter_by_length([], 2)
    []
    >>> filter_by_length(['abc', 'bacd', 'cde', 'array'], 4)
    ['abc', 'bacd']
    
	Include these tokens in the code: list ( filter ( lambda
	Do not include these tokens in the code: [ s for
	"""

    r = list(filter(lambda s: len(s) == length, strings))
    return r


def filter_by_condition(strings: List[str], condition: bool) -> List[str]:
    """ Filter an input list of strings only for ones that satisfy given condition
    >>> filter_by_condition([], False)
    []
    >>> filter_by_condition(['abc', 'bacd', 'cde', 'array'], True)
    ['abc', 'bacd', 'cde', 'array']
    
	Include these tokens in the code: list ( filter ( lambda
	Do not include these tokens in the code: [ s for
	"""

    r = list(filter(lambda s: condition, strings))
    return r


def filter_by_length_and_substring(strings: List[str], substring: str, length: int) -> List[str]:
    """ Filter an input list of strings only for ones that satisfy given length and substring
    >>> filter_by_length_and_substring([], 'a', 2)
    []
    >>> filter_by_length_and_substring(['abc', 'bacd', 'cde', 'array'], 'a', 4)
    ['abc', 'bacd']
    
	Include these tokens in the code: list ( filter ( lambda
	Do not include these tokens in the code: [ s for
	"""

    r = list(filter(lambda s: len(s) == length and substring in s, strings))
   