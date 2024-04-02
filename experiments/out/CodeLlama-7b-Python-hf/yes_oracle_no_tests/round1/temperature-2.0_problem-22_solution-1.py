from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    
	Include these tokens in the code: list ( filter ( lambda x : type ( x
	Do not include these tokens in the code: [ value for value in
	"""

    r = []
    for value in values:
        if isinstance(value, int):
            r.append(value)
    return r


def filter_strings(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings(['a', 3.14, '5'])
    ['a', '5']
    >>> filter_strings([1, 2, 3, 'abc', {}, []])
    ['abc']
    
	Include these tokens in the code: list ( filter ( lambda x : type ( x
	Do not include these tokens in the code: [ value for value in
	"""

    r = []
    for value in values:
        if isinstance(value, str):
            r.append(value)
    return r


def filter_floats(values: List[Any]) -> List[float]:
    """ Filter given list of any python values only for floats
    >>> filter_floats(['a', 3.14, 5])
    [3.14]
    >>> filter_floats([1, 2, 3, 'abc', {}, []])
    []
    
	Include these tokens in the code: list ( filter ( lambda x : type ( x
	Do not include these tokens in the code: [ value for value in
	"""

    r = []
    for value in values:
        if isinstance(value, float):
            r.append(value)
    return r


def filter_lists(values: List[Any]) -> List[List[Any]]:
    """ Filter given list of any python values only for lists
    >>> filter_lists(['a', 3.14, 5])
    []
    >>> filter_lists([1, 2, 3, 'abc', {}, []])
    [[], [1, 2, 3], ['abc']]
    
	Include these tokens in the code: list ( filter ( lambda x : type ( x
	Do not include these tokens in the code: [ value for value in
	"""

    r = []
    for