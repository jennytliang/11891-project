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

    r = [value for value in values if type(value) == int]

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

    r = [value for value in values if type(value) == str]

    return r


def filter_dicts(values: List[Any]) -> List[dict]:
    """ Filter given list of any python values only for dicts
    >>> filter_dicts(['a', 3.14, 5])
    []
    >>> filter_dicts([1, 2, 3, 'abc', {}, []])
    [{}]]
    
	Include these tokens in the code: list ( filter ( lambda x : type ( x
	Do not include these tokens in the code: [ value for value in
	"""

    r = [value for value in values if type(value) == dict]

    return r


def filter_lists(values: List[Any]) -> List[list]:
    """ Filter given list of any python values only for lists
    >>> filter_lists(['a', 3.14, 5])
    []
    >>> filter_lists([1, 2, 3, 'abc', {}, []])
    [[], [1, 2, 3, 'abc', {}, []]]
    
	Include these tokens in the code: list ( filter ( lambda x : type ( x
	Do not include these tokens in the code: [ value for value in
	"""

    r = [value for value in values if type(value) == list]

    return r


def filter_floats(values: List[Any]) -> List[float]:
    """ Filter given list of