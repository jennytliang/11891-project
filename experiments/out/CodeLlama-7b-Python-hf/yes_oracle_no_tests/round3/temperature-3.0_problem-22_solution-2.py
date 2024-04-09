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

    r = list(filter(lambda x: type(x) == int, values))
    return r


def filter_strings(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_integers(['a', 3.14, 5])
    ['a']
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    ['abc']
    
	Include these tokens in the code: list ( filter ( lambda x : type ( x
	Do not include these tokens: [ value for value in
    """

    r = list(filter(lambda x: type(x) == str, values))
    return r


def filter_empty_values(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for empty values
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    
	Include these tokens in the code: list ( filter ( lambda x : type ( x
	Do not include these tokens: [ value for value in
    """

    r = list(filter(lambda x: x == "", values))
    return r


def filter_not_empty_values(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for not empty values
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    
	Include these tokens in the code: list ( filter ( lambda x : type ( x
	Do not include these tokens: [ value for value in
    """

    r = list(filter(lambda x: x != "", values))
    return r


def filter_dicts(values: List[Any]) -> List[dict]:
    """ Filter given list of any python values only