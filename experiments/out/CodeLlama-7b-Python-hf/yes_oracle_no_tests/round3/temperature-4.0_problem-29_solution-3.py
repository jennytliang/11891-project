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
    """ Filter an input list of strings only for ones that are the given length.
    >>> filter_by_length([], 2)
    []
    >>> filter_by_length(['abc', 'bcd', 'cde', 'array'], 3)
    ['abc', 'bcd']
    
	Include these tokens in the code: strings
	Do not include these tokens in the code: string
	"""


    return list(filter(lambda x: len(x) == length, strings))


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain a given substring.
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    
	Include these tokens in the code: strings
	Do not include these tokens in the code: string
	"""


    return list(filter(lambda x: substring in x, strings))


def filter_by_condition(strings: List[str], condition: str) -> List[str]:
    """ Filter an input list of strings only for ones that satisfy a given condition.
    >>> filter_by_condition([], 'len(x) > 2')
    []
    >>>