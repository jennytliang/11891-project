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


def filter_empty_strings(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for empty strings
    >>> filter_empty_strings(['a', 'ab', ''])
    ['']
    >>> filter_empty_strings([1, 2.2, 'abc', ''])
    ['']
    
	Include these tokens in the code: list ( filter ( lambda x : type ( x
	Do not include these tokens in the code: [ value for value in
	"""

    r = []
    for value in values:
        if isinstance(value, str) and len(value) == 0:
            r.append(value)
    return r


def filter_non_empty_strings(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for non-empty strings
    >>> filter_non_empty_strings(['a', 'ab', ''])
    ['a', 'ab']
    >>> filter_non_empty_strings([1, 2.2, 'abc', ''])
    ['abc']
    
	Include these tokens in the code: list ( filter ( lambda x : type ( x
	Do not include these tokens in the code: [ value for value in
	"""

    r = []
    for value in values: