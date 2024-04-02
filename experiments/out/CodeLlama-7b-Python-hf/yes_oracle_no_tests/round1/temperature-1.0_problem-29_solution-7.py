from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    
	Include these tokens in the code: x
	Do not include these tokens in the code: s
	"""

    return list(filter(lambdas, strings))


def filter_by_suffix(strings: List[str], suffix: str) -> List[str]:
    """ Filter an input list of strings only for ones that end with a given suffix.
    >>> filter_by_suffix([], 'a')
    []
    >>> filter_by_suffix(['abc', 'bcd', 'cde', 'array'], 'rray')
    ['array']
    
	Include these tokens in the code: x
	Do not include these tokens in the code: s
	"""

    return list(filter(lambdas, strings))


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that include a given substring.
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bcd', 'cde', 'array'], 'rray')
    ['array']
    
	Include these tokens in the code: x
	Do not include these tokens in the code: s
	"""

    return list(filter(lambdas, strings))


def filter_by_length(strings: List[str], min_length: int, max_length: int) -> List[str]:
    """ Filter an input list of strings only for ones that have a length between a minimum and maximum (inclusive).
    >>> filter_by_length([], 1, 10)
    []
    >>> filter_by_length(['abc', 'bcd', 'cde', 'array'], 3, 4)
    ['abc', 'bcd']
    
	Include these tokens in the code: x
	Do not include these tokens in the code: s
	"""

    return list(filter(lambdas, strings))


def filter_by_length_greater_than(strings: List[str], min_length: int) -> List[str]:
    """ Filter an input list of strings only for ones that have a length greater than a minimum.
    >>> filter_by_length_greater_than