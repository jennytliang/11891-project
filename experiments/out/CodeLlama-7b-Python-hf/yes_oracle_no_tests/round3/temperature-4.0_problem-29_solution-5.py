from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    
	Include these tokens in the code: lambda x : x
	Do not include these tokens in the code: l -> l
	"""


    return list(f for f in strings if f.startswith(prefix))


def filter_by_suffix(strings: List[str], suffix: str) -> List[str]:
    """ Filter an input list of strings only for ones that end with a given suffix.
    >>> filter_by_suffix([], 'a')
    []
    >>> filter_by_suffix(['abc', 'bcd', 'cde', 'array'], 'rray')
    ['array']
    
	Include these tokens in the code: l -> l
	Do not include these tokens in the code: lambda x : x
	"""


    return list(f for f in strings if f.endswith(suffix))


def filter_by_length(strings: List[str], min_length: int, max_length: int) -> List[str]:
    """ Filter an input list of strings only for ones that are between a given minimum and maximum length.
    >>> filter_by_length([], 1, 10)
    []
    >>> filter_by_length(['abc', 'bcd', 'cde', 'array'], 2, 3)
    ['bcd', 'array']
    
	Include these tokens in the code: lambda x : x
	Do not include these tokens in the code: l -> l
	"""


    return list(f for f in strings if min_length <= len(f) <= max_length)


def filter_by_include(strings: List[str], includes: List[str]) -> List[str]:
    """ Filter an input list of strings only for ones that contain all the strings in a given list.
    >>> filter_by_include([], [])
    []
    >>> filter_by_include(['abc', 'bcd', 'cde', 'array'], ['bc', 'de'])
    ['bcd', 'cde']
    
	Include these tokens in the code: l -> l
	Do not include these tokens in the code: lambda x : x
	"""


    return list(f for f in strings if all(i in f for i in includes))


def filter_by