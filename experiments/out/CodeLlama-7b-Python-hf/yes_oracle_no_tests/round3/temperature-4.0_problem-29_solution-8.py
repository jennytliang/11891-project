from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    
	Include these tokens in the code: strings
	Do not include these tokens in the code: string
	"""


    return list(filter(lambda x: x.startswith(prfix), strings))


def filter_by_suffix(strings: List[str], suffix: str) -> List[str]:
    """ Filter an input list of strings only for ones that end with a given suffix.
    >>> filter_by_suffix([], 'a')
    []
    >>> filter_by_suffix(['abc', 'bcd', 'cde', 'array'], 'rray')
    ['array']
    
	Include these tokens in the code: strings
	Do not include these tokens in the code: string
	"""


    return list(filter(lambda x: x.endswith(suffix), strings))


def filter_by_length(strings: List[str], length: int) -> List[str]:
    """ Filter an input list of strings only for ones that have a given length.
    >>> filter_by_length([], 1)
    []
    >>> filter_by_length(['abc', 'bcd', 'cde', 'array'], 4)
    ['bcd', 'array']
    
	Include these tokens in the code: strings
	Do not include these tokens in the code: string
	"""


    return list(filter(lambda x: len(x) == length, strings))


def filter_by_length_range(strings: List[str], min_length: int, max_length: int) -> List[str]:
    """ Filter an input list of strings only for ones that have a length in a given range.
    >>> filter_by_length_range([], 1, 2)
    []
    >>> filter_by_length_range(['abc', 'bcd', 'cde', 'array'], 3, 5)
    ['abc', 'bcd', 'array']
    
	Include these tokens in the code: strings
	Do not include these tokens in the code: string
	"""


    return list(filter(lambda x: min_length <= len(x) <= max_length, strings))


def filter_by_regex(strings: List[str], regex: str) -> List[str]:
    """ Filter an input list