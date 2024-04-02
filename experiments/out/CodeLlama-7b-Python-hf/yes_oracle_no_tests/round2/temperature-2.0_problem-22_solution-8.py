from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    
	Include these tokens in the code: list ( filter ( lambda
	Do not include these tokens in the code: [ x for
	"""

    r = []
    for x in values:
        if isinstance(x, int):
            r.append(x)
    return r


def filter_strings(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings(['a', 3.14, 5])
    ['a']
    >>> filter_strings([1, 2, 3, 'abc', {}, []])
    ['abc']
    
	Include these tokens in the code: list ( filter ( lambda
	Do not include these tokens in the code: [ x for
	"""

    r = []
    for x in values:
        if isinstance(x, str):
            r.append(x)
    return r


def filter_empty_strings(values: List[str]) -> List[str]:
    """ Filter given list of strings only for non-empty ones
    >>> filter_empty_strings(['a', 3.14, 5])
    []
    >>> filter_empty_strings(['', 2, 'abc', {}, []])
    ['abc']
    
	Include these tokens in the code: list ( filter ( lambda
	Do not include these tokens in the code: [ x for
	"""

    r = []
    for x in values:
        if x:
            r.append(x)
    return r


def filter_booleans(values: List[Any]) -> List[bool]:
    """ Filter given list of any python values only for booleans
    >>> filter_booleans(['a', 3.14, 5])
    []
    >>> filter_booleans([1, 2, 3, 'abc', {}, []])
    [True, False]
    
	Include these tokens in the code: list ( filter ( lambda
	Do not include these tokens in the code: [ x for
	"""

    r = []
    for x in values:
        if isinstance(x, bool):
            r.append(x)
    return r


def filter_dicts(values: List[Any])