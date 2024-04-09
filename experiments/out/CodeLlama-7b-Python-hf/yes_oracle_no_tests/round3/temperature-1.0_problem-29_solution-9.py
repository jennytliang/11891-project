from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    
	Include these tokens in the code: prefix
	Do not include these tokens in the code: pr if ix
	"""



    return list(filter(lambda x: x.starstwith(prefix), strings))


def filter_by_suffix(strings: List[str], suffix: str) -> List[str]:
    """ Filter an input list of strings only for ones that end with a given suffix.
    >>> filter_by_suffix([], 'a')
    []
    >>> filter_by_suffix(['abc', 'bcd', 'cde', 'array'], 'rray')
    ['array']
    
	Include these tokens in the code: suffix
	Do not include these tokens in the code: sx if ix
	"""



    return list(filter(lambda x: x.endswith(suffix), strings))


def filter_by_length(strings: List[str], min_length: int, max_length: int) -> List[str]:
    """ Filter an input list of strings only for ones whose length is between the given range (inclusive).
    >>> filter_by_length([], 5, 10)
    []
    >>> filter_by_length(['abc', 'bcd', 'cde', 'array'], 5, 10)
    ['abc', 'bcd', 'cde']
    
	Include these tokens in the code: length
	Do not include these tokens in the code: len if ix
	"""



    return list(filter(lambda x: (len(x) >= min_length) and (len(x) <= max_length), strings))


def filter_by_include(strings: List[str], includes: List[str]) -> List[str]:
    """ Filter an input list of strings only for ones that contain all the strings given in the includes list.
    >>> filter_by_include([], [])
    []
    >>> filter_by_include(['abc', 'bcd', 'cde', 'array'], ['b', 'c'])
    ['bcd', 'cde']
    
	Include these tokens in the code: includes
	Do not include these tokens in the code: inc if ix
	"""



    return list(filter(lambda x: all(i in x for i