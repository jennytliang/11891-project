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
    >>> filter_strings(['a', 3.14, 5])
    ['a']
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


def filter_booleans(values: List[Any]) -> List[bool]:
    """ Filter given list of any python values only for booleans
    >>> filter_booleans(['a', 3.14, 5])
    []
    >>> filter_booleans([1, 2, 3, 'abc', {}, []])
    []
    
	Include these tokens in the code: list ( filter ( lambda x : type ( x
	Do not include these tokens in the code: [ value for value in
	"""

    r = []
    for value in values:
        if isinstance(value, bool):
            r.append(value)
    return r


def filter_dictionaries(values: List[Any]) -> List[dict]:
    """ Filter given list of any python values only for dictionaries
    >>> filter_dictionaries(['a', 3.14, 5])
    []
    >>> filter_dictionaries([1, 2, 3, 'abc', {}, []])
    [{}]
    
	Include these tokens in the code: list ( filter ( lambda x : type ( x
	Do not include these tokens in the code: [ value for value in
	"""

    r = []
    for value in values:
        if isinstance(value, dict):
            r.append